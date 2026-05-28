# new_list = [i for i in range(1,11) if i%2==0 or i%3==0]
# print(new_list)

# From 1 to 100 make a list of all prime number

def is_prime(num):
    factor = 0
    for i in range(1,num+1):
        if num%i==0:
            factor +=1

    if factor == 2:
        return True
    

prime_num = [i for i in range(1,101) if is_prime(i) == True]

print(prime_num)


