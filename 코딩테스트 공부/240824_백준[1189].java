
import java.util.*;

// dfs/컴백홈/실버1

public class Main_1189 {
	static int r,c,k,ans=0;
	static char[][] board;
	static boolean[][] visit;
	static int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}}; //상우하좌
	static StringTokenizer st;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		r = sc.nextInt();
		c= sc.nextInt();
		k = sc.nextInt();
		
		board = new char[r][c];
		visit = new boolean[r][c];
		visit[r-1][0] = true;
		
		for(int i=0;i<r;i++) {
			String tmp = sc.next();
			for(int j=0;j<c;j++) {
				board[i][j] = tmp.charAt(j);
			}
		}
		
		dfs(r-1,0,1);
		System.out.println(ans);
	}
	
	static void dfs(int x,int y, int dist) {
		if(x==0 && y==c-1) {
			if(dist==k) ans++;
			return;
		}
		
		
		for(int i=0;i<4;i++) {
			int mx = x+dir[i][0];
			int my = y+dir[i][1];
			
			if (mx<0 || mx>=r|| my<0 || my>=c) continue;
			
			if(!visit[mx][my] && board[mx][my]=='.') {
				visit[mx][my] = true;
				dfs(mx,my,dist+1);
				visit[mx][my] = false;
			}
		}
		
	}

}
