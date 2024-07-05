
D1 = "new home top forecast"
D2 = "home sales rise in july"
D3 = "increase in home sales july"
D4 = "july new home sales"

collection = [D1,D2,D3,D4]

priority={"not":3,"and":2,"or":1}
Index={}
Buffer_seen={}
values=[0]*100
op=[0]*100

def Process_Query(Query):
  Query_tokens=Query.split(" ")
  track=-1
  move=-1
  for i in Query_tokens:
    if i  in Term_Incedense_Matrix:
        track+=1
        values[track]=Term_Incedense_Matrix[i]
    elif i in priority:
        #print(i)
        if(move==-1):
            move+=1
            op[move]=i
        else:
            # print(i)
            if(priority[op[move]] <= priority[i]):
                move+=1
                op[move]=i
            else:
                #print(op[move])
                while(move >=0 and (priority[op[move]] > priority[i])):
                    if(op[move] == "and"):
                        res=Intersection(values[track-1],values[track])
                        track=track-1
                        move=move-1
                        values[track]=res
                    elif(op[move] == "or"):
                        res=Union(values[track-1],values[track])   
                        track=track-1
                        move=move-1
                        values[track]=res 
                    else:
                        res=Minus(values[track-1],values[track])   
                        track=track-1
                        move=move-1
                        values[track]=res
                move+=1
                op[move]=i 
    else:
        track+=1
        values[track]=[]
  
  while move >= 0:
                    if(op[move] == "and"):

                        res=Intersection(values[track-1],values[track])
                        track=track-1
                        move=move-1
                        values[track]=res
                    elif(op[move] == "or"):
                        res=Union(values[track-1],values[track])  
                        track=track-1
                        move=move-1
                        values[track]=res 
                    else:
                        res=Minus(values[track-1],values[track]) 
                        track=track-1
                        move=move-1
                        values[track]=res
#Tokenisation
tokens = []
for i in collection:
    tokens.extend(i.split())
Term_Incedense_Matrix = {}
for i in tokens:
    Term_Incedense_Matrix[i] = []
    for k in collection:
        if i in k:
            Term_Incedense_Matrix[i].append(1)
        else:
            Term_Incedense_Matrix[i].append(0)
#Intersection
def Intersection(l1,l2):
    res=[]
    for i in range(len(l1)):
        if(l1[i]==1 and l2[i]==1):
            res.append(1)
        else:
            res.append(0)
    return res
#union
def Union(l1,l2):
    res=[]
    for i in range(len(l1)):
        if(l1[i]==1 or l2[i]==1):
            res.append(1)
        else:
            res.append(0)
    return res
#Not
def Minus(l1,l2):
    res=[]
    for i in range(len(l1)):
        if(l1[i]==1 and l2[i]==0):
            res.append(1)
        else:
            res.append(0)
    return res
def Show(l):
    print("the retrieved Documents are : ",end= " ")
    for i in range(len(l)):
        if(l[i]==1):
            print(i+1," -> ",end= " ")
        
#Query Processing
print(Term_Incedense_Matrix)
query = "sales and in not july or forecast"
Query=query
print("Query is : ",query)
Process_Query(query)
Show(values[0])
