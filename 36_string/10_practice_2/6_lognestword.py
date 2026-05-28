def longest_word(sentence):

    words = sentence.split()
    longest_count = 0
    longest_word = ""

    for word in words:
        if len(word) > longest_count:
            longest_count = len(word)
            longest_word = word

    print(longest_word)

sentence = "gsvfj sibifg jndbibid sfnoenfo sdhbfkhf"

ans = longest_word(sentence)

print(ans)


print(max(sentence, key=lambda x : len(x)))
