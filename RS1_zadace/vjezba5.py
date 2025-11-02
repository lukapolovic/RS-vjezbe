# Drugi argument u range funkciji nije ukljucen (2 ne ulazi) tako da ce se ova petlja izvrtiti samo jednom
# Petlja bas i nije petlja ako se ne izvrti barem 2 ili vise puta
for i in range(1, 2):
    print(i)

# Nece ispisati nista jer se loopa krece u pozitivnom smjeru (10 + 2)
for i in range(10, 1, 2):
    print(i)

# Ispisati ce: 10, 9, 8, 7, 6, 5, 4, 3, 2
for i in range(10, 1, -1):
    print(i)