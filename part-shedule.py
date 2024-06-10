
visited = [0] * 8
col=['']*8
person=["","Rayaan","Chandler","Joe","Jef","Ted","Barney","Marshall","Ross"]

def dfs(g,s,d):
    col[s]=d
    visited[s]=1
    
    for i in range(len(g[s])):
        if not visited[g[s][i]]:
            new_col='F' if col[s]=='S' else 'S'
            dfs(g,g[s][i],new_col)
    
            
    


graph = {
    1:[2,3],
    2:[5],
    3:[6,7],
    4:[],
    5:[3],
    6:[],
    7:[]
}

dfs(graph,1,'F')
for i in range(len(col)):
    if col[i] != '':
        day= "Friday" if col[i]=='F' else "Saturday"
        print(person[i],"is scheduled on: ",day)
