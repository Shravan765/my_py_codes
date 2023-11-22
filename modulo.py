#modulo finder for exponents
import time
#O(n) algorithm
def modulo(a, b, n):
    val = 1
    for i in range(b):
        
        val *= a
        if val > n:
            
            val = val%n
           
    return val

#Repeated square algorithm
def mods(a, b, n):
    #getting binary number of b
    bn = str(bin(b))
    bn = bn[2:]
    i = 1
    val = 1
    for s in bn[::-1]:
        
        #print(val , i)
        if (int(s)):
            val *= pow(a,i)
            #print(val, pow(a,i))
        if val > n:   
            val = val%n
        i*= 2
    return val
        

base = int(input("Enter base : "))
exp = int(input("Enter exponent : "))
n = int(input("Enter n of mod n : "))
t = time.time()
m = modulo(base,exp,n)
print("Time taken by 1st method : ",time.time()-t)
print(base,"^",exp," ( mod ",n," ) = ", m)
t = time.time()
m1 = mods(base,exp,n)
print("Time taken by 2nd method : ",time.time()-t)
print(base,"^",exp," ( mod ",n," ) = ", m1)
