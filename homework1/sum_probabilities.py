#Modify the program to find and print the sum of all 
#the entries in the list p.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

p[0]=p[0]*pMiss
p[1]=p[1]*pHit
p[2]=p[2]*pHit
p[3]=p[3]*pMiss
p[4]=p[4]*pMiss

# Enter your code below
sum_p = 0
for p_value in p :
    sum_p += p_value

print sum_p

# ALTERNATIVE SOLUTION: sum(p) :( Easier...