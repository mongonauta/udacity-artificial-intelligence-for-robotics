#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
for index in [0, 3, 4] :
    p[index] *= pMiss

for index in [1, 2] :
    p[index] *= pHit
    
print p