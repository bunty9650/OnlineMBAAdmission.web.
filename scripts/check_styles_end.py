with open('styles.css', 'r', encoding='utf-8') as f:
    c = f.read()

print("File size:", len(c))
print("End of file:")
print(c[-600:])
