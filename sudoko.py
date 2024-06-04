def solve_sudoku(arr):
    n = len(arr)
    return solver(arr, n)
    

def solver(arr,n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                for s in range(1,n+1):
                    if check(arr,i,j,s):
                        arr[i][j]=s
                        if solver(arr,n):
                            return True
                        arr[i][j]=0
                return False
    return True


def check(arr,i,j,num):
    return (not used_row(arr,i,num) and not used_col(arr,j,num) and not used_grid(arr,i-i%3,j-j%3,num))
    

def used_in_row(arr, row, num):
    return num in arr[row]

            
def used_row(arr,i,num):
    return num in arr[i]
    
def used_col(arr,j,num):
    return any(row[j] == num for row in arr)
    


def used_grid(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False

if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    if solve_sudoku(sudoku_grid):
        print("Sudoku Solved:")
        for row in sudoku_grid:
            print(row)
    else:
        print("No solution exists.")
        
        
