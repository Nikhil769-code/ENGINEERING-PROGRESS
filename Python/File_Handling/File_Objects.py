# -------------------- File Objects --------------------

f = open('test.txt', 'r')
# Opens file in read mode
# Provide full path if file is in another directory

print(f.name)   # File name
print(f.mode)   # Mode in which file is opened

f.close()  
# Always close file manually if not using context manager


# -------------------- Context Manager --------------------

# Best practice:
# - Automatically closes file
# - Prevents resource leaks (too many open files)

with open('test.txt', 'r') as f:
    f_contents = f.read()
    # Reads entire file as a single string
    print(f_contents)


with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    # Reads all lines → returns list
    print(f_contents)


# -------------------- Reading with Control --------------------

with open('test.txt', 'r') as f:

    f_contents = f.read()
    # Reads full content
    print(f_contents)

    f_contents = f.read(100)
    # Reads next 100 characters (after previous read → likely empty)
    print(f_contents)

    size_to_read = 10

    f_contents = f.read(size_to_read)
    # Reads next 10 characters
    print(f_contents, end='*')

    # File pointer moves forward after each read
    # To re-read from start → reset pointer

    f.seek(0)
    # Moves pointer back to beginning

    f_contents = f.read(size_to_read)
    print(f_contents)

    print(f.tell())
    # Current position of pointer in file


    # -------------------- Reading in Chunks --------------------

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
    # Efficient for large files


    # -------------------- Iterating Line by Line --------------------

    for line in f:
        print(line, end='')
        # Reads one line at a time (memory efficient)

    f_contents = f.readline()
    print(f_contents)
    # Reads one line
    # Repeated calls read next lines sequentially


# -------------------- Writing to File --------------------

with open('test2.txt', 'w') as f:
    # 'w' mode:
    # - Overwrites file if exists
    # - Creates new file if not

    f.write('Test')

    f.seek(0)
    # Moves pointer to beginning

    f.write('Test')
    # Overwrites from start


# -------------------- Copy File --------------------

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
    # Copies content line by line