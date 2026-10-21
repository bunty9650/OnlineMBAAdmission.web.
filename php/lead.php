<?php
// php/lead.php - Secure Hostinger Production Lead Capture & CRM Forwarder
declare(strict_types=1);

// 1. Strict CORS & Security Headers
$allowedOrigins = [
    "https://www.onlinembaadmission.com",
    "https://onlinembaadmission.com",
    "https://onlinembaadweb.vercel.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
];

$origin = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origin !== '') {
    if (in_array($origin, $allowedOrigins, true) || str_ends_with($origin, '.vercel.app')) {
        header("Access-Control-Allow-Origin: " . $origin);
        header("Vary: Origin");
    } else {
        http_response_code(403);
        header("Content-Type: application/json; charset=UTF-8");
        echo json_encode(['success' => false, 'error' => 'Origin not allowed by CORS policy']);
        exit;
    }
} else {
    header("Access-Control-Allow-Origin: https://www.onlinembaadmission.com");
}

header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: SAMEORIGIN");
header("Referrer-Policy: strict-origin-when-cross-origin");
header("Content-Type: application/json; charset=UTF-8");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed. Use POST.']);
    exit;
}

// 2. IP Rate Limiting (5 requests per 10 minutes per IP)
$clientIp = $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? 'unknown';
if (strpos($clientIp, ',') !== false) {
    $clientIp = trim(explode(',', $clientIp)[0]);
}

$rateLimitWindow = 600; // 10 minutes
$maxRequests = 5;
$cacheDir = sys_get_temp_dir();
$rateFile = $cacheDir . '/rate_lead_' . md5($clientIp) . '.json';

$isLimited = false;
$now = time();
if (file_exists($rateFile)) {
    $rateData = json_decode((string)file_get_contents($rateFile), true);
    if (is_array($rateData) && isset($rateData['reset'], $rateData['count'])) {
        if ($now < $rateData['reset']) {
            if ($rateData['count'] >= $maxRequests) {
                $isLimited = true;
            } else {
                $rateData['count']++;
                @file_put_contents($rateFile, json_encode($rateData), LOCK_EX);
            }
        } else {
            @file_put_contents($rateFile, json_encode(['count' => 1, 'reset' => $now + $rateLimitWindow]), LOCK_EX);
        }
    } else {
        @file_put_contents($rateFile, json_encode(['count' => 1, 'reset' => $now + $rateLimitWindow]), LOCK_EX);
    }
} else {
    @file_put_contents($rateFile, json_encode(['count' => 1, 'reset' => $now + $rateLimitWindow]), LOCK_EX);
}

if ($isLimited) {
    http_response_code(429);
    echo json_encode([
        'success' => false,
        'error' => 'Too many lead submissions from your network. Please wait a few minutes before trying again or contact admissions@onlinembaadmission.com.'
    ]);
    exit;
}

try {
    $rawInput = file_get_contents('php://input');
    $data = json_decode((string)$rawInput, true);

    if (!is_array($data)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Invalid JSON payload']);
        exit;
    }

    // 3. Honeypot Check
    if (!empty($data['website']) || !empty($data['honeypot']) || !empty($data['company_url']) || !empty($data['fax'])) {
        http_response_code(200);
        echo json_encode(['success' => true, 'message' => 'Lead processed']);
        exit;
    }

    // Sanitization Helper
    $sanitize = function($val, $maxLen = 100) {
        $s = strip_tags((string)($val ?? ''));
        $s = str_replace(['<', '>', '{', '}', '\\', '/'], '', $s);
        $s = preg_replace('/\s+/', ' ', $s);
        return mb_substr(trim($s), 0, $maxLen);
    };

    $name = trim((string)($data['name'] ?? ''));
    $mobileRaw = trim((string)($data['mobile'] ?? $data['phone'] ?? ''));
    $email = strtolower(trim((string)($data['email'] ?? '')));
    $detail1 = $sanitize($data['detail1'] ?? $data['program'] ?? 'Online MBA', 200);
    $detail2 = $sanitize($data['detail2'] ?? '', 500);
    $consent = $data['consent'] ?? false;

    // 4. Mandatory Consent Check
    if ($consent !== true && strtolower((string)$consent) !== 'true' && $consent !== 1 && $consent !== '1') {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'Consent is mandatory. User must agree to be contacted by OnlineMBAAdmission counsellors.'
        ]);
        exit;
    }

    // 5. Unicode-Aware Name Validation
    if (!preg_match('/^[\p{L}\p{M}\s\.\'\-]{2,60}$/u', $name)) {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'Please provide a valid full name (2 to 60 characters, letters only).'
        ]);
        exit;
    }
    $name = $sanitize($name, 60);

    // 6. Normalize Mobile Phone
    $mobileDigits = preg_replace('/\D/', '', $mobileRaw);
    if (strlen($mobileDigits) === 12 && substr($mobileDigits, 0, 2) === '91') {
        $mobileDigits = substr($mobileDigits, 2);
    } elseif (strlen($mobileDigits) === 11 && substr($mobileDigits, 0, 1) === '0') {
        $mobileDigits = substr($mobileDigits, 1);
    }

    if (!preg_match('/^[6-9]\d{9}$/', $mobileDigits)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Please provide a valid 10-digit Indian mobile number']);
        exit;
    }

    // 7. Email Validation
    if (!filter_var($email, FILTER_VALIDATE_EMAIL) || strlen($email) > 100) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Please provide a valid email address']);
        exit;
    }

    if (empty($detail2)) {
        $detail2 = 'Consent: Granted for University Admission Counselling | Version: 2026.1 | Timestamp: ' . gmdate('Y-m-d\TH:i:s\Z');
    }

    // 8. Forward to CRM strictly via Environment Variable (No hardcoded secrets)
    $crmUrl = trim((string)(getenv('NEODOVE_LEADS_URL') ?: ''));
    $crmForwarded = false;
    $crmStatusCode = null;

    if (!empty($crmUrl)) {
        $crmPayload = json_encode([
            'name'    => $name,
            'mobile'  => (int)$mobileDigits,
            'email'   => $email,
            'detail1' => $detail1,
            'detail2' => $detail2
        ]);

        if (function_exists('curl_init')) {
            $ch = curl_init($crmUrl);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $crmPayload);
            curl_setopt($ch, CURLOPT_HTTPHEADER, [
                'Content-Type: application/json',
                'User-Agent: OnlineMBAAdmission-Hostinger-Proxy/1.0'
            ]);
            curl_setopt($ch, CURLOPT_TIMEOUT, 10);
            $response = curl_exec($ch);
            $crmStatusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            $crmForwarded = ($crmStatusCode >= 200 && $crmStatusCode < 300);
            curl_close($ch);
        } else {
            $options = [
                'http' => [
                    'method'  => 'POST',
                    'header'  => "Content-Type: application/json\r\nUser-Agent: OnlineMBAAdmission-Hostinger-Proxy/1.0\r\n",
                    'content' => $crmPayload,
                    'timeout' => 10
                ]
            ];
            $context = stream_context_create($options);
            $result = @file_get_contents($crmUrl, false, $context);
            if ($result !== false) {
                $crmForwarded = true;
                $crmStatusCode = 200;
            }
        }
    }

    http_response_code(200);
    echo json_encode([
        'success' => true,
        'message' => 'Lead received successfully',
        'forwarded_to_crm' => $crmForwarded,
        'crm_status_code' => $crmStatusCode
    ]);

} catch (Throwable $t) {
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'error' => 'Internal server error processing lead'
    ]);
}
