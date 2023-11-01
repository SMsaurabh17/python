

# conditional statement
# if statement
numT = 17
if(numT > 0 and numT <= 5):
    print('5% discount')
if(numT > 5 and numT <= 10):
    print('10% discount')
if(numT > 10):
    print('15% discount')


# 2 using if and elif

marks = 93
if marks >= 90:
    print('grade a')
elif marks >= 70:
    print('grade b')
elif marks >= 50:
    print('grade c')
else:
    print('fail')



# 3

s = 10
t = 50
if s > t:
    print('s is greater')
else:
    print('t is greater')


# ternary operator (it can be used only when there is only one expresssion)

print('s is greater') if s > t else print('t is greater')