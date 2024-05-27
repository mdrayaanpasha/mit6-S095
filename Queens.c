// Online C compiler to run C program online
#include <stdio.h>
#include <stdbool.h>

#define N 4


bool authorized(int arr[N][N],int row,int col){
    int i,j;
    for(i=0;i<N;i++){
        if(arr[i][col] || arr[row][i]){
            return false;
        }
    }
    
    for (i=row,j=col; i>=0 && j>=0;i--,j--){
        if(arr[i][j]){
            return false;
        }
    }
    
    for(i=0,j=col;i>=0 && j<N ;i--,j++){
        if(arr[i][j]){
            return false;
        }
    }
    
    for(i=0,j=col;i<0 && j<N ;i++,j++){
        if(arr[i][j]){
            return false;
        }
    }
    
    for(i=0,j=col;i<0 && j>=0 ;i++,j--){
        if(arr[i][j]){
            return false;
        }
    }
}

void printArr(int arr[N][N]){
    for(int i =0;i<N;i++){
        for(int j=0;j<N;j++){
            printf("%d",arr[i][j]);
        }
        printf("\n");
    }
}

void fourQueens(){
    int arr[N][N] = {0};
    
   
    
    for(int i=0;i<N;i++){
        arr[i][0]=1;
        for(int j=0;j<N;j++){
            arr[j][1]=1;
            if(authorized(arr,j,1)){
                for(int k=0;k<N;k++){
                    arr[k][2]=1;
                    if(authorized(arr,k,2)){
                        for(int m=0;m<N;m++){
                            arr[m][3]=1;
                            if(authorized(arr,m,3)){
                                printArr(arr);
                                break;
                            }
                            arr[m][3]=0;
                        }
                    }
                    arr[k][2]=0;
                }
            }
            arr[j][1]=0;
        }
        arr[i][0]=0;
    }
    
}

int main() {
    fourQueens();
    return 0;
}
