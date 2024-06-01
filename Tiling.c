#include <stdio.h>

#define N 8 
void recurase(int arr[N][N], int RS, int RE, int CS, int CE, int ist, int jst) {
    if (RE - RS == 1) {
        for (int i = RS; i < RS + 1; i++) {
            for (int j = CS; j < CS + 1; j++) {
                if (arr[i][j] == -1) {
                    arr[i][j] = 1; 
                }
            }
        }
    } else {
        int rowmid = (RS + RE) / 2;
        int colmid = (CS + CE) / 2;

      
        if (jst < rowmid && ist < colmid) {
            arr[colmid + 1][rowmid] = 1;
            arr[colmid][rowmid + 1] = 1;
            arr[colmid + 1][rowmid + 1] = 1;
            
            recurase(arr, RS, rowmid, CS, colmid, ist, jst);
            recurase(arr, rowmid + 1, RE, CS, colmid, colmid, rowmid + 1);
            recurase(arr, RS, rowmid, colmid + 1, CE, colmid + 1, rowmid);
            recurase(arr, rowmid + 1, RE, colmid + 1, CE, colmid + 1, rowmid + 1);
        } 
        if (jst > rowmid && ist < colmid) {
            arr[colmid + 1][rowmid] = 1;
            arr[colmid][rowmid] = 1;
            arr[colmid + 1][rowmid + 1] = 1;

            recurase(arr, RS, rowmid, CS, colmid, colmid, rowmid);
            recurase(arr, RS, rowmid, colmid + 1, CE, rowmid, colmid + 1);
            recurase(arr, rowmid + 1, RE, CS, colmid, ist, jst);
            recurase(arr, rowmid + 1, RE, colmid + 1, CE, colmid + 1, rowmid + 1);
        } 
        if (jst < rowmid && ist > colmid) {
            arr[colmid + 1][rowmid + 1] = 1;
            arr[colmid][rowmid] = 1;
            arr[colmid][rowmid + 1] = 1;

            recurase(arr, RS, rowmid, CS, colmid, colmid, rowmid);
            recurase(arr, RS, rowmid, colmid + 1, CE, ist, jst);
            recurase(arr, rowmid + 1, RE, CS, colmid, rowmid, colmid);
            recurase(arr, rowmid + 1, RE, colmid + 1, CE, colmid + 1, rowmid + 1);
        } 
        if (jst > rowmid && ist > colmid) {
            arr[colmid][rowmid + 1] = 1;
            arr[colmid][rowmid] = 1;
            arr[colmid + 1][rowmid] = 1;

            recurase(arr, RS, rowmid, CS, colmid, colmid, rowmid);
            recurase(arr, RS, rowmid, colmid + 1, CE, rowmid, colmid + 1);
            recurase(arr, rowmid + 1, RE, CS, colmid, colmid, rowmid + 1);
            recurase(arr, rowmid + 1, RE, colmid + 1, CE, ist, jst);
        }
    }
}

int main() {
    int arr[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            arr[i][j] = -1;
        }
    }

    int ist = 4, jst = 6;  
    recurase(arr, 0, N, 0, N, ist, jst);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%2d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
