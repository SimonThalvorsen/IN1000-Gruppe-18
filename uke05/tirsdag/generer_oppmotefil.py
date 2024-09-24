import random

fil = open("oppmøte_in1000.txt", "w")

# Skriver den første linjen med grupper
for i in range(8):
    # Siste gruppe skal ikke ha semikolon bak seg
    if i == 7:
        fil.write("Gruppe_" + str(i+1))
        fil.write("\n")
    else:
        fil.write("Gruppe_" + str(i+1) + ";")

# Nøsta for-løkker for å skrive 12 linjer med 8 tall hver
for i in range(12):
    for j in range(8):
        # Tilfeldig tall fra 0 til 31
        antall = random.randint(0, 31)
        if j == 7:
            # Siste tallet skal ikke ha semikolon bak seg
            fil.write(f"{antall}")
        else:
            fil.write(f"{antall};")
    fil.write("\n")

fil.close()
