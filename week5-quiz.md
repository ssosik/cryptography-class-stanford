---
author: {author}
date: {date}
tags:
- work
title: {title}
---


# 5 7a+23b=1
7 * 10 + 23 * -3 = 1
70 - 69 = 1
a = 10
b = -3

7^-1 in Z23 => a*x + b*N = 1 => a*x = 1 in ZN => x^-1 = a in ZN

Answer:
10,-3,10

# 6
Solve the equation 3x + 2 = 7 in Z19

x = 3
N = 19

a * 3 + b * 19 = 1
a = 13
b = -2

 x=(7−2)×3^−1 ∈Z 19

 5 * 13

 Answer: 65
 Answer: 8

# 7 Size of Z*35

Count of all numbers that are relatively prime to 35; gcd(x,N) = 1
exclude 5,7,10,14,15,20,21,25,28,30,35
35-11 => 24

Answer: 24


#11 Which of the following numbers is a generator of \mathbb{Z}_{13}^*Z 13 ∗ ​	?
```python
p=13
g=2
len([math.pow(g,i)%p for i in range(1,p)])

for g in range(1,p):
  print("{} : {}".format(g, len(set([math.pow(g,i)%p for i in range(1,p)]))))


# 10
p=35
g=2
>>> len(set([math.pow(g,i)%p for i in range(1,p)]))
12
# Answer; 12
```

#14 
Answer 9
2^9 mod 13 == 5
