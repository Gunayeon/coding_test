message=input()
playfair=input()
alphabet='ABCDEFGHIKLMNOPQRSTUVWXYZ'

alphabet_dict={}
for i in range(len(alphabet)):
    alphabet_dict[alphabet[i]]=0


for i in range(len(playfair)):
    alphabet_dict[playfair[i]]+=1


playfair_arr=[[0]*5 for _ in range(5)]
r=0
c=0
for i in range(len(playfair)):
    if alphabet_dict[playfair[i]]>0:
        playfair_arr[r][c]=playfair[i]
        alphabet_dict[playfair[i]]=-1
        c+=1
        if c==5:
            c=0
            r+=1

for i in alphabet:
    if alphabet_dict[i]==0:
        playfair_arr[r][c]=i
        c+=1
        if c==5:
            c=0
            r+=1
print(playfair_arr)


def maketwofair(msg):
    two_fair=[]
    for i in range(0,len(msg),2):
        if i+1<len(msg):
            two_fair.append(msg[i]+msg[i+1])
        elif i+1>=len(msg):
            two_fair.append(msg[i])
    return two_fair
 



def insertXorQ(two_fair):
    
   
    sum_message=''
    i=0
    cnt=0
    while True:
        if i==len(two_fair):
            break
        if len(two_fair[i])==2:
            if two_fair[i][0]==two_fair[i][1] and cnt==0:
                if two_fair[i]!='XX':
                    two_fair[i]=two_fair[i][0]+'X'+two_fair[i][1]
                    cnt+=1
                else:
                    two_fair[i]=two_fair[i][0]+'Q'+two_fair[i][1]
                    cnt+=1
       
        i+=1
  
    for i in range(len(two_fair)):
        sum_message+=two_fair[i]

    return sum_message


def checkfair(lst):
    if len(lst)%2!=0:
        lst+='X'
    result_fair=[]
    for i in range(0,len(lst),2):
        result_fair.append(lst[i]+lst[i+1])

    return result_fair


change=checkfair(insertXorQ(maketwofair(message)))
print(change)

def checkdupli(lst):
    for i in range(len(lst)):
        if lst[i][0]==lst[i][1]:
            return False
    return True

while True:
    print(change)
    check=False
    for i in range(len(change)):
        if change[i][0]==change[i][1]:
            check=True
            
    if check==True:
        change=checkfair(insertXorQ(maketwofair(change)))
        
    if checkdupli(change):
        break

def checksamerow(lst):
    for i in range(5):
        if lst[0] in playfair_arr[i] and lst[1] in playfair_arr[i]:
            return i+1
    return False

def checksamecol(lst):
    for i in range(5):
        column=[row[i] for row in playfair_arr]
        
        if lst[0] in column and lst[1] in column:
            return i+1
    return False



def changesamerow(lst,row):
    result=[0]*len(lst)
    for i in range(5):
        if lst[0]==playfair_arr[row][i]:
            result[0]=playfair_arr[row][(i+1)%5]
        if lst[1]==playfair_arr[row][i]:
            result[1]=playfair_arr[row][(i+1)%5]
    return result[0]+result[1]
    

def changesamecol(lst,col):
    result=[0]*len(lst)
    for i in range(5):
        if lst[0]==playfair_arr[i][col]:
            result[0]=playfair_arr[(i+1)%5][col]
        if lst[1]==playfair_arr[i][col]:
            result[1]=playfair_arr[(i+1)%5][col]
    return result[0]+result[1]

def changenotsamerowcol(lst):
    row1=0
    col1=0
    row2=0
    col2=0
    result=[0]*len(lst)
    for i in range(5):
        for j in range(5):
            if lst[0]==playfair_arr[i][j]:
                row1=i
                col1=j
            if lst[1]==playfair_arr[i][j]:
                row2=i
                col2=j
    result[0]=playfair_arr[row1][col2]
    result[1]=playfair_arr[row2][col1]

    return result[0]+result[1]



result=''
for i in range(len(change)):
    if checksamerow(change[i]):
        result+=changesamerow(change[i], checksamerow(change[i])-1)
    elif checksamecol(change[i]):
        result+=changesamecol(change[i],checksamecol(change[i])-1)
    else:
        result+=changenotsamerowcol(change[i])
print(result)
