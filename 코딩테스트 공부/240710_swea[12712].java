import java.util.Scanner;
import java.io.FileInputStream;
 
 // 배열제어/파리퇴치3/D2

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int n,m;
        int[][] board;
        int[] killer;
         
        for (int tc = 1; tc < T+1; tc++) {
            n = sc.nextInt();
            m = sc.nextInt();
  
            board = new int[n][n];
            killer =new int[n*n*2];
            int ans=1;
            int cnt=0;
            int idx=0;
             
            for(int i = 0 ; i<n ; i++) {
                for(int j = 0 ; j<n ; j++) {
                    board[i][j]=sc.nextInt();
                }
            }
 
            for(int i=0 ; i<n ; i++) {
                for(int j=0 ;j<n ;j++) {
                    //파리1
                    cnt = board[i][j];
                    for(int k = 1 ; k <m ; k++) {
                        if (i-k >= 0) cnt += board[i-k][j];
                        if (i+k < n) cnt += board[i+k][j];
                        if (j-k >= 0) cnt += board[i][j-k];
                        if (j+k < n) cnt += board[i][j+k];
                    }
                     
                    killer[idx++] = cnt;
                     
                  //파리2
                    cnt = board[i][j];
                    for(int k = 1 ; k <m ; k++) {
                        if (j+k < n && i-k >= 0) cnt += board[i-k][j+k];
                        if (j-k >= 0 && i+k < n) cnt += board[i+k][j-k];
                        if (j+k < n && i+k < n) cnt += board[i+k][j+k];
                        if (j-k >= 0 && i-k >= 0) cnt += board[i-k][j-k];
                    }
                     
                    killer[idx++] = cnt;
                }
            }
             
            for(int i=0 ; i < (n*n*2) ; i++) {
                ans = Math.max(ans,killer[i]);
            }
             
            System.out.printf("#%d %d\n",tc,ans);
        }
    }
}