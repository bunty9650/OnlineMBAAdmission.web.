<?php
// api/lead.php - Hostinger Production Lead Capture & CRM Forwarder
declare(strict_types=1);

// Set CORS & Content-Type
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json; charset=UTF-8");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(204);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit;
}

try {
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    if (!is_array($data)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Invalid JSON payload']);
        exit;
    }

    $name = trim((string)($data['name'] ?? ''));
    $mobileRaw = trim((string)($data['mobile'] ?? $data['phone'] ?? ''));
    $email = trim((string)($data['email'] ?? ''));
    $detail1 = trim((string)($data['detail1'] ?? $data['program'] ?? 'Online MBA'));
    $detail2 = trim((string)($data['detail2'] ?? ''));
    $consent = $data['consent'] ?? false;

    // 1. Mandatory Consent Check
    if ($consent !== true && strtolower((string)$consent) !== 'true' && $consent !== 1 && $consent !== '1') {
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'error' => 'Consent is mandatory. User must agree to be contacted by OnlineMBAAdmission counsellors.'
        ]);
        exit;
    }

    // 2. Name Validation
    if (mb_strlen($name) < 2) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Name must be at least 2 characters']);
        exit;
    }

    // 3. Normalize Phone
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

    // 4. Email Validation
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'error' => 'Please provide a valid email address']);
        exit;
    }

    if (empty($detail2)) {
        $detail2 = 'Consent: "I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry." | Submitted: ' . gmdate('Y-m-d\TH:i:s\Z');
    }

    // 5. Forward to NeoDove CRM
    $crmUrl = getenv('NEODOVE_LEADS_URL') ?: 'https://3092a01d-31a6-46a0-a092-11aa63948adc.neodove.com/integration/custom/fa17b06f-23c3-4928-8dc3-0ae7fedcd09f/leads';
    $crmForwarded = false;
    $crmStatusCode = null;

    $crmPayload = json_encode([
        'name'    => mb_substr($name, 0, 100),
        'mobile'  => (int)$mobileDigits,
        'email'   => mb_substr($email, 0, 100),
        'detail1' => mb_substr($detail1, 0, 200),
        'detail2' => mb_substr($detail2, 0, 500)
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
