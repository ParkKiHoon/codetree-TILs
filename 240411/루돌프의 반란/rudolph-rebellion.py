n, m, p, c, d = map(int,input().split())
rr, rc = map(int,input().split())
rr-=1
rc-=1
santa = []
board=[[-1 for _ in range(n)] for _ in range(n)]
stun=[0 for i in range(p)]
for i in range(p):
    tmp=list(map(int,input().split()))
    santa.append([tmp[1]-1,tmp[2]-1,0,1])
    board[tmp[1]-1][tmp[2]-1]=i

for i in range(n):
    print(board[i])
print(santa)
print(rr,rc)

def distance(r1,c1,r2,c2):
    return (r1-r2)**2 + (c1-c2)**2

def move_dolph(r1,c1):
    santa_num=0
    santa_pos=[0,0]
    minval=9999999999
    for i in santa:
        if i[3]==0:
            continue
        r2,c2=i[0],i[1]
        dist=distance(r1,c1,r2,c2)
        if dist<minval:
                minval=dist
                santa_pos=r2,c2
        elif dist==minval:
            if r2>santa_pos[0]:
                santa_pos=r2,c2
            elif r1==r2 and c2>santa_pos[1]:
                santa_pos=r2,c2

    return santa_pos

def move_dolph_rule(r1,c1,r2,c2):
    if r1>r2:
        r1-=1
    elif r1<r2:
        r1+=1

    if c1>c2:
        c1-=1
    elif c1<c2:
        c1+=1

    return r1,c1

def interaction(dr,dc,r2,c2):
    r22=r2+dr
    c22=c2+dc
    ind = board[r2][c2]
    santa[ind] = [r22, c22, santa[ind][2] + 1, santa[ind][3]]
    board[r2][c2] = -1
    if 0<=r22<n and 0<=c22<n:
        if board[r22][c22] != -1:
            interaction(dr,dc,r22,c22)
            board[r22][c22]=ind
    else:
        santa[ind][3]=0
def move_dolph_collide(dr,dc,r2,c2):
    r22=r2+dr
    c22=c2+dc
    ind = board[r2][c2]
    santa[ind] = [r22, c22, santa[ind][2] + c, santa[ind][3]]
    board[r2][c2] = -1
    if 0<=r22<n and 0<=c22<n:
        if board[r22][c22] != -1:
            interaction(dr,dc,r22,c22)
            board[r22][c22]=ind
            stun[ind]=2
    else:
        santa[ind][3]=0

def move_santa(r1,c1,rr,rc):
    santa_pos=[-1,-1]
    minval=9999999999
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for i in range(4):
        x=r1+dx[i]
        y=c1+dy[i]
        if 0<=x<n and 0<=y<n and board[x][y]==-1:
            dist_after=distance(x,y,rr,rc)
            dist_before=distance(r1,c1,rr,rc)
            if dist_after < dist_before:
                if dist_after<=minval:
                        minval=dist_after
                        santa_pos=x,y
    return santa_pos

def move_santa_collide(dr,dc,r2,c2):
    r22=r2+dr
    c22=c2+dc
    ind = board[r2][c2]
    santa[ind] = [r22, c22, santa[ind][2] + c, santa[ind][3]]
    board[r2][c2] = -1
    if 0<=r22<n and 0<=c22<n:
        if board[r22][c22] != -1:
            interaction(dr,dc,r22,c22)
            board[r22][c22]=ind
            stun[ind]=2
    else:
        santa[ind][3]=0

for times in range(1):
    r2,c2=move_dolph(rr,rc)
    r1,c1=move_dolph_rule(rr,rc,r2,c2)
    dr,dc=r1-rr,c1-rc
    rr,rc=r1,c1
    if r1==r2 and c1==c2:
        move_dolph_collide(dr,dc,r2,c2)
    for i in range(p):
        if santa[i][3]==0 or stun[i]>0:
            pass
        else:
            x,y=(move_santa(santa[i][0],santa[i][1],rr,rc))
            if [x,y]==[-1,-1]:
                pass
            else:
                move_santa_collide()

        stun[i]-=1

    for i in range(n):
        print(board[i])

    print(santa)
    print(rr,rc)
    print(stun)