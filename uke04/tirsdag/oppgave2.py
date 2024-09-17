import random

tall_liste = []
for i in range(10):
    tall_liste.append(i)

for i in range(0, len(tall_liste), 2):
    print(tall_liste[i], end=" ")
print()

# Eller

for tall in tall_liste:
    if tall % 2 == 0:
        print(tall, end=" ")
print()

liste = []
for i in range(10):
    liste.append(random.randint(0, 100))


# Her kan vi ikke bruke den løkken som stepper over oddetall, siden vi ikke vet om listen 
# har elementer på format: partall, oddetall, partall osv
for tall in liste:
    if tall % 2 == 0:
        print(tall, end=" ")
print()
