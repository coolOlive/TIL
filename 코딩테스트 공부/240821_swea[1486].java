import java.io.*;
import java.util.*;

// 장훈이의 높은 선반/d4

class Solution
{
	static StringTokenizer st;
	static int T,n,b,ans;
	static int[] height;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for(int tc=1;tc<T+1;tc++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			height = new int[n];
			ans = Integer.MAX_VALUE;
			
			st = new StringTokenizer(br.readLine());
			for(int i = 0;i<n;i++) {
				height[i] = Integer.parseInt(st.nextToken());
			}
			Arrays.sort(height);

			find(0,0);
			System.out.println("#"+tc+" "+ans);
		}
	}
	
	static void find(int cnt, int sum) {
        if(cnt == n) {
            if(sum >= b) ans = Math.min(ans,sum-b);
            return;
        }
         
        find(cnt+1, sum+height[cnt]);
        find(cnt+1, sum);
    }
}