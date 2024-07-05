D1 = "new home top forecast"
D2 = "home sales rise in july"
D3 = "increase in home sales july"
D4 = "july new home sales"
collection=[D1,D2,D3,D4]
priority={"not":3,"and":2,"or":1}
Index={}
Buffer_seen={}
values=[0]*100
op=[0]*100
class Node:
    def __init__(self,data=-1):
        self.docId=data
        self.next=None

def Make():
    k=1
    for i in collection:
        try:
            Saw(i,k)
            k+=1
        except TypeError:
            print("Error: Invalid data type in collection")
            return

def Saw(string,Id):
    if not isinstance(string, str):
        raise TypeError("Input string should be a string")
    tokens=string.split(" ")
    for i in tokens:
        if i not in Index:
            c=Node(Id)
            Index[i]=c
        else:
            c=Index[i]
            while(c.next != None):
                c=c.next
            cs=Node(Id)
            c.next=cs

def Intersection(a,b):
    k=1
    flag=0
    while(a != None and b != None):
        if(a.docId == b.docId):
            if k==1:
                flag=1
                common=Node(a.docId)
                k+=1
            else:
                c=common
                while(c.next!=None):
                    c=c.next
                c.next=Node(a.docId)
            a = a.next
            b = b.next
        elif a.docId < b.docId:
            a = a.next
        else:
            b = b.next
    if flag==0:
        return None
    return common

def Union(a,b):
    k=1
    flag=0

    while(a != None and b != None):
        if(a.docId == b.docId):
            if k==1:
                flag=1
                common=Node(a.docId)
                prev=common
                k+=1
            else:
                prev.next=Node(a.docId)
                prev=prev.next
            a = a.next
            b = b.next
        elif a.docId < b.docId:
                if k==1:
                    flag=1
                    common=Node(a.docId)
                    prev=common
                    k+=1
                else:
                  prev.next=Node(a.docId)
                  prev=prev.next
                a = a.next
        else:
                if k==1:
                    flag=1
                    common=Node(b.docId)
                    prev=common
                    k+=1
                else:
                  prev.next=Node(b.docId)
                  prev=prev.next
                b = b.next
    while(b):
           if k==1:
                flag=1
                common=Node(a.docId)
                prev=common
                k+=1
           else:
                prev.next=Node(a.docId)
                prev=prev.next
           b = b.next

    while(a):
          if k==1:
                flag=1
                common=Node(a.docId)
                prev=common
                k+=1
          else:
                prev.next=Node(a.docId)
                prev=prev.next
          a = a.next
    if flag==0:
            return None
    return common

        
#Minus
def Minus(a,b):
    k=1
    flag=0
    temp = []
    res = []
    while(b != None):
        temp.append(b.docId)
        b = b.next
    while(a != None):
        if(a.docId not in  temp):
            if k==1:
                flag=1
                common=Node(a.docId)
                prev=common
                k+=1
            else:
                prev.next=Node(a.docId)
                prev=prev.next
        a = a.next
    if flag==0:
            return None
    return common

def Process_Query(Query):
  Query_tokens=Query.split(" ")
  track=-1
  move=-1
  for i in Query_tokens:
    if i  in Index:
        track+=1
        values[track]=Index[i]
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
                while(move >=0 and (priority[op[move]] > priority[i]) ):
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
                Print(res)
                move+=1
                # print(move)
                op[move]=i 
    else:
        track+=1
        values[track]=None
  
  while move >= 0:
                    print(op[move])
                    if(op[move] == "and"):

                        res=Intersection(values[track-1],values[track])
                        track=track-1
                        move=move-1
                        values[track]=res
                    elif(op[move] == "or"):
                        Print(values[track-1])
                        res=Union(values[track-1],values[track])  
                        Print(res)  
                        track=track-1
                        move=move-1
                        values[track]=res 
                    else:
                        res=Minus(values[track-1],values[track]) 

                        Print(res) 
                        track=track-1
                        move=move-1
                        values[track]=res


def Print(a):
    flag=0
    while(a!=None):
        flag=1
        print(a.docId," - > ",end=" ")
        a=a.next
    if flag==0:
        print("No Search Results Found :(")
    print()

def Process(a):
    seen={}
    flag=0
    while(a!=None):
        if(flag==0):
            print("The retrieved Documents are : ")
        flag=1
        if(a.docId not in seen):
            print(a.docId," - > ",end=" ")
            seen[a.docId]=1
        a=a.next
    if flag==0:
        print("No Search Results Found :(")
    print()


if(__name__=="__main__"):
    Make()
    # for i in Index.keys():
    #   print(i,end=" ")
    #   Print(Index[i])
    Query="new and sales or forecast and july not increase"
    Process_Query(Query)
    Process(values[0])
