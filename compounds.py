perc1 = float(input("Percent Compound 1"))
perc2 = 100-perc1

AMU1 = 12.011
AMU2 = 15.999

mol1 = perc1 / AMU1
mol2 = perc2 / AMU2


if mol1 > mol2:
    print(f"comp 1 / comp 2 = {mol1 /mol2}")
else:
    print(f"comp 2 / comp 1 = {mol2 / mol1}")
