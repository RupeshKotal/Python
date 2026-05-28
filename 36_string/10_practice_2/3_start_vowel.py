# def count_vowel(sentence:str):
#     vow = "aeiou"
#     vowels = vow.split()
#     len_v = len(vowels)
#     words = sentence.split()
#     len_w = len(words)
#     total = 0
#     for v in range(0,len_v):
#         for w in range(0,len_w):
#             if words[w].startswith(vowels[v]):
#                 total += 1
#     return total

# sentence = "My name is rupesh what is your name and my fav animal is elephane"

# ans = count_vowel(sentence)

# print(ans)



# def count_vow(sentence):
#     vowel = "aeiou"
#     words = sentence.lower().split()

#     total = 0

#     for word in words:
#         if word.startswith(tuple(vowel)):
#             total +=1

#     return total

# sentence = "hellow a ksjnfiu adjuf hin uo huj eoor oudj"

# ans = count_vow(sentence)
# print(ans)


def count_vow(sentence):
    vowels = "aeiou"
    words = sentence.split()
    total = 0
    for word in words:
        if word[0] in vowels:
            total += 1

    return total


sentence = "hellow a ksjnfiu adjuf hin uo huj eoor oudj"

ans = count_vow(sentence)