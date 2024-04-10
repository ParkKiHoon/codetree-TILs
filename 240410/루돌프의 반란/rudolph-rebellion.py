n, m, p, c, d = map(int,input().split())
Rr, Rc = map(int,input().split())
santa = []
for i in range(p):
    tmp=list(map(int,input().split()))
    santa.append([tmp[1]-1,tmp[2]-1])
board=[[0 for _ in range(n)] for _ in range(n)]
print(board)
print(santa)

def distance(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2

def move_dolph(r1,c1):
    santa_num=0
    santa_pos=[0,0]
    minval=9999999999
    for i in santa:
        r2,c2=i
        dist=distance(r1,c1,r2,c2)
        if dist<minval:
                minval=dist
                santa_num=i
                santa_pos=r2,c2
        elif dist==minval:
            if r2>santa_pos[0]:
                santa_num=i
                santa_pos=r2,c2
            elif r1==r2 and c2>santa_pos[1]:
                santa_num=i
                santa_pos=r2,c2

    return (santa_pos)
print(move_dolph(2,1))