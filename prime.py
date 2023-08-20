#prime printing

def prime_gen(n1, n2):
    #n1, n2 INCLUSIVE
    plst = [] #list of prime number
    for i in range(n1,n2+1):
        k = 1 #key , which assumes here i is prime
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                k = 0 #sends message that i IS NOT prime
                break
        if k:
            plst.append(i)
    return plst

#main

str1 = '''
->  This program will generate all prime numbers between starting
    and ending point you will give.
->  Note that both starting and ending pint are included.


'''
print(str1)
n1, n2 = int(input("Enter starting point : ")), int(input("Enter ending point : "))
lst = prime_gen(n1, n2)
    
with open("primebook.txt", "a") as fin:
    str2 = "Entry : from "+str(n1)+" to "+str(n2)+" : \n"
    fin.write(str(str2))
    for i in lst:
        fin.write(str(i))
        fin.write("\n")
    fin.write("\nDONE\n\n\n")

print("\nDONE.........")
        
        
