import os

if not (os.path.exists("dummy")):
    os.mkdir("dummy")

# for i in range(0,3):
#     os.mkdir(f"dummy/demo-{i+1}")


# for i in range(0,3):
    # os.rename(f"dummy/demo-{i+1}", f"dummy/day-{i+1}")


'''
folders = os.listdir("dummy")

for folder in folders:
    print(folder)
    print(os.listdir(f"dummy/{folder}"))

'''

print(os.getcwd())
os.chdir('/Desktop')

print(os.list.dir())



