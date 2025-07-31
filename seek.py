with open("Records.txt", "w") as f:
    f.write("HELLLLLO")

with open("Records.txt", "rb") as f:
    print(f.read()) #for reading the whole file the file must be opened in binary mode cause "r" mode doesnt support negative offset
    f.seek(3) # Move the cursor to the 4th character
    print(f.read())
    f.seek(-1, 2) # Move the cursor to the last character
    print(f.read())
    f.close()

#syntanx is f.seek(offset, whence) where offset is the number of bytes to move and whence is the reference point (0 for start, 1 for current position, 2 for end).
