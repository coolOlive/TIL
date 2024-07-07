import java.util.Scanner;
import java.io.FileInputStream;
 
// 완전탐색/두 개의 숫자열/D2

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int n, m, ans, plusTmp;
        int[] A, B;
         
        for (int tc=1;tc<T+1;tc++) {
            n = sc.nextInt();
            m = sc.nextInt();
            A = new int[n];
            B = new int[m];
            ans = 0;
             
            for(int i = 0; i < n; i++) {
                A[i] = sc.nextInt();
            }
             
            for(int i = 0; i < m; i++) {
                B[i] = sc.nextInt();
            }
             
            if (n > m) {
                int tmp = n;
                int[] tmpArr = A;
                n = m;
                m = tmp;
                A = B;
                B = tmpArr;
            }
             
            for (int j = 0;j<Math.abs(m-n)+1;j++) {
                plusTmp = 0;
                for (int k = 0;k<n;k++) {
                    plusTmp += (A[k]*B[j+k]);
                }
                if (ans<plusTmp) ans = plusTmp;
            }
            System.out.printf("#%d %d\n",tc,ans);
        }
    }
}