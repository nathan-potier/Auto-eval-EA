entree = [8 ,  47  , 22 ,  29  , 12  , 26  , 19  , 10 ,  7 ,  11 ,  31]
mod = 7



res = {}

for e in entree :
    t = e % mod
    if t in res :
        
        res[t]+= 1
    else :
        res[t] = 1
        


res = dict(sorted(res.items()))
print (res)