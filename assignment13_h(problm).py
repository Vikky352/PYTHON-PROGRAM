res=[]
def permutate(n,i,l):
    if i==l:
        res.append(''.join(n))
    else:
        for j in range(i,l):
            n[i],n[j]=n[j],n[i]
            permutate(n,i+1,l)
            n[i],n[j]=n[j],n[i]

n=input("enter String: ")
permutate(list(n),0,len(n))
print("Permutation: \n",str(res))