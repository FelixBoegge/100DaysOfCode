# practice read from and write to files
# open a file in write mode "w", if file does not exist, it will be created
f = open("file_practice.txt", "w")
f.write("Hello World\n")
f.close()

# open file and append content "a"
f = open("file_practice.txt", "a")
f.write("Use of append mode\n")
for i in range(10):
    f.write(f"This is line {i+1}\n")
f.close()

# open file in read mode "r"
f = open("file_practice.txt", "r")
if f.mode == "r":
    content = f.read()
    print(content)
f.close()

# open file in read mode and read file line by line
f = open("file_practice.txt", "r")
f1 = f.readlines()
for x in f1:
    if x.startswith("This"):
        print(x)
f.close()
