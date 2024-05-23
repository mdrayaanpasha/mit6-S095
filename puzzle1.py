
caps= ['f','f','f','b','b','f','b','b','b','f','f','f','b']

def conform(caps):
    start = 0
    back = 0
    front = 0
    intervals = []
    for i in range(1,len(caps)):
        if caps[i]!= caps[start]:
            intervals.append((start,i-1,caps[start]))
            if caps[i]=='f':
                front+=1
            else:
                back+=1
            start = i
    intervals.append((start,len(caps)-1,caps[i]))
    if caps[start]=='f':
        front+=1
    else:
        back+=1
    if front > back:
        flip='b'
    else:
        flip='f'
    
    for t in intervals:
        if t[2]==flip:
            print("folks from ",t[0],"to ",t[1],"please change your orientation!")
            
            
def optimizedConform(caps):
    start = 0
    front =0
    back =0
    intervals =[]
    caps = caps + ['END']
    
    for i in range(len(caps)):
        
        if caps[start]!=caps[i]:
            intervals.append((start,i-1,caps[start]))
            
            front = front + 1 if caps[start] == 'f' else front
            back = back + 1 if caps[start] == 'b' else back
            start = i
    
    # Determine which caps to flip
        flip = 'b' if front > back else 'f'
        
        for t in intervals:
            if t[2] == flip:
                print("Flip from: ",t[0]," to: ",t[1])
            
            
def compact(caps):
    caps = caps + [caps[0]]
    
    for i in range(len(caps)):
        if caps[i] != caps[i-1]:
            if caps[0]!= caps[i]:
                print("folks start fliping from: ",i," to: ")
            else:
                print("to: ",i-1)
    
# conform(caps)
# optimizedConform(caps)
compact(caps)
        
            
    
        
