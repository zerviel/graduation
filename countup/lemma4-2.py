
i = 0
j = 0
k = 0
h = 0
r = 0
s = 0
t = 0
u = 0
lam = [2][2][2][2][2][2][2][2]
lam = 1

for i in range(2):
    for j in range(2):
        for k in range(2):
            for h in range(2):
                for r in range(2):
                    for s in range(2):
                        for t in range(2):
                            for u in range(2):
                                if i==j:
                                    lam = 0
                                if k==h:
                                    lam = 0
                                if r==s:
                                    lam = 0
                                if t==u:
                                    lam = 0
                                if lam != 0:
                                    print(i,j,h,k,r,s,t,u)

                                    
                                
