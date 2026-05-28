#Local Variable
'''
def local_var(n1,n2,n3=4):
    total = n1 + n2 + n3 #local variable
    return total

ans = local_var(4,n2=6) 
print(ans)
'''

#Global variable

count = 1

def increse():
    global count
    count += 1
    print(f"print {count}")

increse()