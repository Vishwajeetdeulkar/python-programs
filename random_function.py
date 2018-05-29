import random

for i in range(10):
 x = random.random()  #random() function prints values from 0.0 to 1.0 excluding 1.0
 print x


print(random.randint(5, 10)) #print b/w low and high given as arguments

t = [1, 2, 3]
print(random.choice(t)) #To choose an element from a sequence at random, you can use choice

