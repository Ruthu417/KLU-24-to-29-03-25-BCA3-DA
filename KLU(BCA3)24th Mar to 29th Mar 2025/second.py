def is_prime(n):
    fc=0
    for dig in range(1,n//2+1):
        if n%dig==0:
            fc+=1
    if fc==1:
        return True
    else:return False
    
    
#is_prime(10)
print('working with r+ mode')