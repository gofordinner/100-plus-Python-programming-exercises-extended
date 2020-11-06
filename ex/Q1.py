# Question 1

### **Question:**

# > **_Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# > between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line._**

'''
answerNumbers = []
a = 2000
while a < 3201:
    if (a%7== 0) and (a%5!=0):
    # (a % 7 == 0) and (a % 5 != 0):
        answerNumbers.append(a)
    a += 1

print(answerNumbers)
'''


l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))
