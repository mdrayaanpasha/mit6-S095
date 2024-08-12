
def check(BS):
    for keys in BS:
        if len(BS[keys]) not 1:
            return false
        
    return true
    
def rejected(BR,G,B):
    G = BR[G]
    
    for i in range(len(G)):
        if G[i] == B:
            return True
    
    return False

def removeBad(g,available,prefrence,BR):
    highest = available[0]
    
    for i in range(len(available)):
        if available[i] > highest:
            highest = available[i]
            
    
    #eliminate not highest, and add them in rejected!
    available[0]=highest
    for i in range(len(available)):
        if available[i] != highest and i not 0:
            BR[g].append(available[i])
            available[i]=None
            

def algorithm(GP,BP,BS,BR):
    counter=0;
    
    while not check(BS):
        #search for the counter rank in each boy, if there then insert it in the BS list if not in BR.
        for i in range(len(BP)):
            for j in range(len(BP)):
                if BP[i][j] == counter & !rejected(BR,BP[i][j],i):
                    #if not rejected then append them in the BS.
                    BS[BP[i][j]].append(i)
                    
        #till now i have added all folks accorig to their convience and this will hapeen in every round now i need to evaluate
        
        for keys in BS:
            BS[keys] = removeBad(keys,BS[keys],GP[keys],BR)
    


GP : [
[0,3,1,2],
[3,0,1,2],
[0,3,2,1],
[1,2,0,3]
]


BP:[
    [0,2,3,1],
    [0,1,2,3],
    [1,2,0,3],
    [1,2,3,0]
]

BS:{
    0:[],
    1:[],
    2:[],
    3:[]
}

BR:{
    0:[],
    1:[],
    2:[],
    3:[]
}
