
def coins(row,memo):
    if len(row)==0:
        memo[0]=0
        return (0,memo)
    if len(row)==1:
        memo[1]=row[0]
        return (row[0],memo)
    if len(row) in memo:
        return (memo[len(row)],memo)
    
    
    else:
        pick=coins(row[2:],memo)[0]+row[0]
        skip=coins(row[1:],memo)[0]
        result=max(pick,skip)
        return (result,memo)
        
row=[2,1,2,4,5,6,1]
r=coins(row,{})
print(r[0])
