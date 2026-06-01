"""
r = read
w = write
a = append
t = text (open file in text format)
b = open file in binary format (images, pdfs, etc)
"""

# FILE reading

# f = open('50_my-text-file.txt', 'r')
# print(f)
# text = f.read()
# print(text)
# f.close()


# File writing

# f = open("my_file.txt", "w")
# f.write("Hello world")
# f.close()

# # appending a file
# f = open("my_file.txt", "a")
# f.write("Hello world")
# f.close()

#With open
with open('my_file.txt', 'a') as f:
    f.write("My name is rupesh")
