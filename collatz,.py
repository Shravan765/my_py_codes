'''
For a given number checking collatz conjecture
For more information : https://en.wikipedia.org/wiki/Collatz_conjecture
'''

def colchk(n):
    lst = [n,]
    while n != 1:
        if n%2 == 0:
            n= n/2
        else:
            n = 3*n+1
        lst.append(n)
    return lst

#main

print("\nEnter number and check collatz conjecture. For more information : ")
print("https://en.wikipedia.org/wiki/Collatz_conjecture\n")
num1 = int(input("Enter the number : "))
lst = colchk(num1)
print("\nResults : ")
if lst[len(lst)-3:len(lst)]== [4,2,1]:
    print("\nThe collatz conjecture is satisfied by the number ", num1)
    print("The number of steps : ", len(lst)-1)
    print("Highest value attained in process : " , max(lst))
    ask = input("\nwant to see all numbers : y/n")
    if ask.lower() == 'y':
        for i in lst:
            print(i)
    else:
        print("Okay")
else:  #should not be the case for numbers upto 2^68 ≈ 2.95×10^20.
    print("The number doesnt follow collatz conjecture")

#WARNING
'''this program is designed with the intention of verification and not checking
Collatz conjecture, if disproved, can end for example in infinite circular loop
which i havent accounted for.'''
    
