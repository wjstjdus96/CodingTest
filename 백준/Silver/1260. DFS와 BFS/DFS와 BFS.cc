#include <stdio.h>
#define MAX 1001

void DFS(int v, int n);
void BFS(int v, int n);

int Graph[MAX][MAX] = {0};
int DFS_v[MAX] = {0};
int BFS_v[MAX] = {0};
int queue[MAX];

int main(void){
  int N, M, Start;
  int i, x, y;

  scanf("%d%d%d", &N, &M, &Start);

  for(i = 0; i < M; i++){
    scanf("%d%d", &x, &y);
    Graph[x][y] = 1;
    Graph[y][x] = 1;
  }
  DFS(Start, N);
  printf("\n");
  BFS(Start, N);

  return 0;
}

void DFS(int v, int n){
  int i;

  DFS_v[v] = 1;
  printf("%d ", v);
  for(i = 1; i <= n; i++){
    if(Graph[v][i] == 1 && DFS_v[i] == 0){
      DFS(i,n);
    }
  }
  return;
}

void BFS(int v, int n){
  int front = 0, rear = 0, pop, i;

  printf("%d ", v);
  queue[0] = v;
  rear++;
  BFS_v[v] = 1;

  while(front < rear){
    pop = queue[front];
    front++;

    for(i = 1; i <= n; i++){
      if(Graph[pop][i] == 1 && BFS_v[i] == 0){
        printf("%d ", i);
        queue[rear] = i;
        rear++;
        BFS_v[i] = 1;
      }
    }
  }
  return;
}