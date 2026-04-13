# 1. Write mode (w) → create/overwrite file
with open("Codingal.txt", "w") as f:
    f.write("Hello Students!\n")
    f.write("This is write mode.\n")

# 2. Read mode (r) → read file
print("Reading file (r mode):")
with open("Codingal.txt", "r") as f:
    print(f.read())

# 3. Append mode (a) → add data at end
with open("Codingal.txt", "a") as f:
    f.write("This line is added using append mode.\n")

# 4. Read + Write mode (r+)
with open("Codingal.txt", "r+") as f:
    content = f.read()
    f.seek(0)  # move cursor to beginning
    f.write("Modified using r+ mode.\n" + content)

# Final read to show changes
print("Final file content:")
with open("Codingal.txt", "r") as f:
    print(f.read())