name = "rupesh"

def first_last(text):

    first = text[0]
    last = text[-1]
    length = len(text)

    return first, last, length


first, last, length = first_last(name)
print(first)
print(last)
print(length)