# str = 'hello python'
#
# print(str)


def getNum(a):
    if(a<=2):
        return 1
    else:
        return getNum(a-1) + getNum(a-2)


# print(getNum(10))

for i in range(1,11):
    print(getNum(i),end="\t")