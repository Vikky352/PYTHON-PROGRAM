def hcf(sm,gr):
    if gr==0:
        return sm
    elif sm==0:
         return gr
    elif sm==gr:
        return sm
    elif sm>gr:
        return hcf(sm-gr,gr)
    return hcf(sm,gr-sm)
n,m=[int(c) for c in input("enter two number ").split(',')]
print("hcf of two number is",hcf(n,m))