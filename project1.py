#finding factorial of a number
fact=int(input('enter your number'))
sum=1
for i in range(1,fact):
    if fact<0:
        sum='negative number doesn\'t have factorial'
    elif fact==0:
        sum=1
    else:
        sum*=i
print(sum)