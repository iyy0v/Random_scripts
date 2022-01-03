import random

i = random.randrange(1,9)
j = (i + i)*i

x = random.randrange(i*i,j*j)
y = (x + x)*x

a = random.randrange(x*x,y*y)
b = (a + a)*a

print("Your random number is :" + str(random.randrange(a,b)))
