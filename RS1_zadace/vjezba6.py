# Suma svih parnih brojeva do 100
sum = 0

for num in range(2, 101, 2):
    sum += num
print(f"For loop sum: {sum}")

sum = 0
number = 0
while(True):
    number += 2
    if(number > 100):
        break
    sum += number
print(f"While loop sum: {sum}")


# Prvih 10 neparnih brojeva u obrnutom redoslijedu
for num in range(19, 0, -2):
    print(num)

number = 19
while(True):
    print(number)
    number -= 2
    if(number == 1):
        print(number)
        break;

#Fibonaccijev niz do 1000
n = 1000
a = 0
b = 1
next = b
count = 1

print("\n\nWhile loop fibonacci:\n")
while count <= n:
    print(f"{next}  ")
    count += 1
    a, b = b, next
    next = a + b

print("\n\For loop fibonacci:\n")
for i in range(n+1):
    print(f"{next}  ")
    count += 1
    a, b = b, next
    next = a + b