chaine = """

15   08   55   25   41   21   20   13   16   09   22


"""
entree = [int(x) for x in chaine.split()]

mod = 7

affichage = [1,2,3,0,1,0,4]

res = [0] * mod

for e in entree :
    t = e % mod

    res[t]+= 1

        



print (res)
print(res == affichage)