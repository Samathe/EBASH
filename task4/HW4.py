#1
#Answer: [2,2,2]

#2
#Answer: [1, 2, 2]

#3
#Answer: 4.2

n = int(input())
a = []
for i in range(n):
    item = int(input())
    a = a + [item]
print(sum(a)/len(a))

#4
#Answer:  32
 
n = int(input())
m = int(input())
a = []
for i in range(n):
    item = int(input())
    a = a + [item]
print(a[m])

#5
#Answer: 6

n = int(input())
a = []

for i in range(n):
    item = int(input())
    a = a + [item]

print(sum(a[::2]))