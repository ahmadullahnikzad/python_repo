#first import random module
import random
print(random.random())
#prints integer numbers
print(random.randint(2,20))
#prints float numbers
print(random.uniform(2,20))
#we can set out own number by seed() function
# random.seed(4)
# print(random.randint(5, 20))
#we can produce our favorite choice from a sequence
numbers=[1,2,3,4,5,6,7,8,9]
print(random.choice(numbers))
print(random.choice('ahmad'))
#we can produce random number by step
print(random.randrange(2,20,2))
#we can shuffle mutable sequence
nums=['a','apple','b','banana','c','cat']
random.shuffle(nums)
print(nums)
#we can generate sequence numbers
print(random.sample(range(100),3))
