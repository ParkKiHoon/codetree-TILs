from collections import deque
l, q = map(int,input().split())
orders=[list(input().split()) for _ in range(q)]
table=deque(deque() for _ in range(l))

people={}
prev, cnt=0,0
for order in orders:
    table.rotate(int(order[1])-prev)
    prev=int(order[1])

    if order[0]=='100':
        table[int(order[2])].append((order[3]))
        cnt+=1

    if order[0]=='200':
        if int(order[2]) not in people:
            people[int(order[2])] = [order[3], int(order[4])]
        elif people[int(order[2])][0] == "":
            people[int(order[2])] = [order[3], int(order[4])]

    for i in range(l):
        sub_list=[]
        while table[i]:
            cur_name=table[i].popleft()

            if i in people and people[i][0]==cur_name:
                if people[i][1]>0:
                    people[i][1]-=1
                    cnt-=1
                if people[i][1]==0:
                    people[i][0]=""
            else:
                sub_list.append(cur_name)
        for sub in sub_list:
            table[i].append(sub)

    if order[0]=='300':
        people_cnt=0
        for a,b in people.items():
            if b[0]!="":
                people_cnt+=1

        print(people_cnt,cnt)