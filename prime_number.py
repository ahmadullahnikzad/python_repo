nums=int(input())
status=None
for i in range(2,nums):
    if nums>1:
        if nums%i==0:
            status='Not Prime'
            break
        else:
            status='Prime'
print(status)