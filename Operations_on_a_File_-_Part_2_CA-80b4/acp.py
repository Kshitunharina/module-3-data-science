# Create file with multiple lines
with open("Codingal.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python Programming\n")
    f.write("File Handling\n")

# 1. Read one line using readline()
with open("Codingal.txt", "r") as f:
    print("Using readline():")
    print(f.readline())

# 2. Read multiple lines
with open("Codingal.txt", "r") as f:
    print("Reading multiple lines:")
    for line in f:
        print(line.strip())

# 3. Read first 5 characters
with open("Codingal.txt", "r") as f:
    print("\nFirst 5 characters:")
    print(f.read(5))

# 4. Remove a specific character (remove 'o')
with open("Codingal.txt", "r") as f:
    data = f.read()

data = data.replace("o", "")   # remove 'o'

with open("Codingal.txt", "w") as f:
    f.write(data)

# Final output
print("\nAfter removing 'o':")
with open("Codingal.txt", "r") as f:
    print(f.read())