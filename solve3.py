import numpy as np

r1_list=list(np.arange(0.01,25,0.001))
r2_list=list(np.arange(0.01,25,0.001))
r3_list=list(np.arange(0,100,0.001))

def inv(num):
    try:
        res=num**-1
        return res
    except:
        None

R1T=20
R2T=21
R3T=22

#R1=R1T-(R2**(-1)+R3**(-1))**(-1)
#R1=R1T-inv(inv(R2)+inv(R3))
#R2=R2T-(R1**(-1)+R3**(-1))**(-1)
#R2=R2T-inv(inv(R2)+inv(R3))
#R3=R3T-(R1**(-1)+R2**(-1))**(-1)
#R3=R3T-inv(inv(R1)+inv(R2))

#R1=R1T-(R2**(-1)+(R3T-(R1**(-1)+R2**(-1))**(-1))**(-1))**(-1)

#R2=R2T-(R1**(-1)+(R3T-(R1**(-1)+R2**(-1))**(-1))**(-1))**(-1)


#for n in rango:
#    a=1-(2/7)*n
#    b=(3/4)*n
#    if abs(a-b)<0.001:
#        print(n)


for r1 in r1_list:
    for r2 in r2_list:
        try:
            #print("r1=",r1)
            #print("r2=",r2)
            R1=R1T-(r2**(-1)+(R3T-(r1**(-1)+r2**(-1))**(-1))**(-1))**(-1)
            R2=R2T-(r1**(-1)+(R3T-(r1**(-1)+r2**(-1))**(-1))**(-1))**(-1)
            if abs(R1-r1)<0.001 and abs(R2-r2)<0.001:
                print("R1=",r1)
                print("R2=",r2)
        except:
            None


#R1=R1T-(R2**(-1)+R3**(-1))**(-1)
#R1=R1T-inv(inv(R2)+inv(R3))
#R2=R2T-(R1**(-1)+R3**(-1))**(-1)
#R2=R2T-inv(inv(R2)+inv(R3))
#R3=R3T-(R1**(-1)+R2**(-1))**(-1)
#R3=R3T-inv(inv(R1)+inv(R2))


r1=12.66
r2=14.06

R1=R1T-(r2**(-1)+(R3T-(r1**(-1)+r2**(-1))**(-1))**(-1))**(-1)
R2=R2T-(r1**(-1)+(R3T-(r1**(-1)+r2**(-1))**(-1))**(-1))**(-1)
R3=R3T-inv(inv(r1)+inv(r2))

print("R1=",R1,"R2=",R2,"R3=",R3)


