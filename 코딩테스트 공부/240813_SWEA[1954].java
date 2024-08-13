import java.util.Scanner;
import java.io.FileInputStream;

// 재귀/달팽이 숫자/d2

class Solution
{
    static int T,n,cnt;
    static int[][] snail;
    static boolean[][] visited;
    static int[] dx = {0,1,0,-1};//오하왼위
    static int[] dy = {1,0,-1,0};
     
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        T = sc.nextInt();
         
        for(int tc=1;tc<=T;tc++) {
            n = sc.nextInt();
            snail = new int[n][n];
            visited = new boolean[n][n];
            snail[0][0] = 0;
            visited[0][0] = true;
            cnt=1;
            makeSnail(0,0,0);
             
            if(n%2==0) {
                snail[n/2][n/2-1] = n*n;
            } else {
                snail[n/2][n/2] = n*n;
            }
             
            System.out.printf("#%d\n",tc);
            for(int i=0;i<n;i++) {
                for (int j=0;j<n;j++) {
                    System.out.printf("%d ",snail[i][j]);
                }
                System.out.println();
            }
        }
    }
     
    private static void makeSnail(int x,int y,int d) {
        if(cnt==n*n) return;
         
        snail[x][y] = cnt++;
        visited[x][y] = true;
         
        int mx = x+dx[d]; //이동할 곳
        int my = y+dy[d];
         
        if(mx>=0 && mx<n &&my>=0 && my<n && !visited[mx][my]) { //범위 안쪽이면
             makeSnail(mx, my, d);
        } else {
            // 방향을 전환
            d = (d+1) % 4;
            mx = x + dx[d];
            my = y + dy[d];
            if (mx >= 0 && mx < n && my >= 0 && my < n && !visited[mx][my]) {
                makeSnail(mx, my, d);
            }
        }
    }
}