marks_1 = {
    "science" : 98,
    "english": 50,
    "hindi": 62,
    "marathi": 52,
    "math": 32
}

mark_2 = {
    "geograpy" : 98,
    "history": 50,
    "socail_science": 62,
}


def merge_dic(dic_1, dic_2):
    new_dic={}

    new_dic.update(dic_1)

    new_dic.update(dic_2)

    return new_dic

ans = merge_dic(marks_1, mark_2)
print(ans)
