#To Compute the Total BookMark....

cases = input()
ans = []
for o in range(int(cases)):
        x = input()
        #print(x)
        y = x.split()
        t = [[0*j for j in range(int(y[1]))]for k in range(int(y[0]))]
        for i in range(int(y[0])):
                for l in range(int(y[1])):
                        if (i+l)%2 == 0:
                                t[i][l] = 'W'
                        else:
                                t[i][l] = 'B'
        t[0][0] = 'B'
        if int(y[0])%2 == 1 and int(y[1])%2 == 1:
                t[-1][-1] = 'B'
        ans.append(t)
for p in range(int(cases)):
        for w in range(len(ans[p])):
                print("".join(ans[p][w]))
