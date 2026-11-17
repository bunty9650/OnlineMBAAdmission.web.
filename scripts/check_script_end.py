with open('script.js', 'r', encoding='utf-8') as f:
    c = f.read()

print("File size:", len(c))
print("End of script.js:")
print(c[-600:])
