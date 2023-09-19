#2 body collisions at speeds <<<<< C


def inp(): #takes all input
    try:
        m1 = abs(float(input("Enter mass of 1st object : ")))
        v1 = float(input("Enter velocity of 1st object : "))
        m2 = abs(float(input("Enter mass of 2nd object : ")))
        v2 = float(input("Enter velocity of 2nd object : "))
        dis = float(input("Enter distance between 1st and 2nd : "))
        e = float(input("Enter coeff. of restitution : "))
        
        if e>1 or e<0: #as e is always between 0 and 1
            print("Invalid Entry of e. Program Terminated.")
        else:
            lst = [m1, v1, m2, v2, dis, e]
            phy(lst)
            
    except ValueError:
        print("Wrong Entry of data. Program teriminated.")

def phy(lst):
    #does calculations
    
    time = -1 #if collision happens in infinite time (no collision),  -1
    m1, v1, m2, v2, dis, e = lst
    
    if dis >= 0: #m2 is ahead of m1
            
            if (v2) >= (v1):
                #no collision case
                flst = [m1, v1, m2, v2, time] 
                out(lst, flst)
                
            else:
                #COLLISION OCCOURS
                #finding time for collision
                rv = v1-v2
                time = dis/rv
                #time found

                #conservation of momentum
                
                pi = m1*v1 + m2*v2
                
                vf1 = ((pi) - (rv)*e*(m2) )/ (m1+m2)

                vf2 = ( (pi) + (rv)*e*(m1) )/ (m1+m2)
                #solution found
                flst = [m1, vf1, m2, vf2, time]
                out(lst, flst)
                
                
    else: #m1 is ahead of m2
            if v1 >= v2:
                #no collision case
                flst = [m1, v1, m2, v2, time] 
                out(lst, flst)
            else:
                #COLLISION OCCOURS
                #finding time for collision
                rv = v2-v1
                time = (-dis)/rv #as dis is -ve here
                #time found

                #conservation of momentum
                
                pi = m1*v1 + m2*v2
                
                vf1 = ( (pi) + (rv)*e*(m2) )/ (m1+m2)

                vf2 = ( (pi) - (rv)*e*(m1) )/ (m1+m2)
                #solution found
                flst = [m1, vf1, m2, vf2, time]
                out(lst, flst)
                


                
def out(lst, flst):
    if flst[4] <0:
        print("No collision occours.")
    else:
        print("Collision occours at time : ", round(flst[4], 3))
        
    print("Quantity\t\t","Initial\t\t", "Final")
    print("Mass (1st)\t\t",round(lst[0],3),"\t\t", round(flst[0],3))
    print("Velocity (1st)\t\t",round(lst[1],3),"\t\t", round(flst[1],3))
    print("Mass (2nd)\t\t",round(lst[2],3),"\t\t", round(flst[2],3))
    print("Velocity (2nd)\t\t",round(lst[3],3),"\t\t", round(flst[3],3))





#############################################

string = '''

Two body collision problem in one dimension

=>  No friction, air resistance, etc
=>  Value of mass will be taken with modulus
=>  -VE sign for velocity implies that object is moving in a direction opposite
    to whatever direction you assume for +ve velocity
=>  +VE distance implies 2nd object is ahead of 1st by such distance
    For cases where 1st object needs to be ahead, use -ve distance
=>  For coeff of restitution, if e not in [0,1],
    Then program will Terminate
=>  Decimal input is ACCEPTED FOR ALL 
    
'''

print(string)

inp()
