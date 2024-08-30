import java.io.*;
import java.util.*;

// 그리디/행렬/실버1

public class Main {
	static StringTokenizer st;
	static int[][] board;
	static int[][] board2;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		board = new int[n][m];
		board2 = new int[n][m];
		int ans = 0;
		
		//board 2개 입력받기
		for(int i=0;i<n;i++) {
			String tmp = br.readLine();
			for(int j=0;j<m;j++) {
				board[i][j] = tmp.charAt(j)-'0'; //-'0'꼭 빼먹지 말자
			}
		}
		
		for(int i=0;i<n;i++) {
			String tmp2 = br.readLine();
			for(int j=0;j<m;j++) {
				board2[i][j] = tmp2.charAt(j)-'0';
			}
		}
		
		
		for(int i=0;i<n-2;i++) {
			for(int j=0;j<m-2;j++) {
				if(board[i][j] != board2[i][j]) {
					ans++;
					change(i,j);
				}
			}
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if(board[i][j]!=board2[i][j]) {
					System.out.println(-1);
					return;
				}
			}
		}
		
		System.out.println(ans);

	}
	
	static void change(int x, int y) {
		for(int i=x ; i <x+3 ; i++) {
			for(int j=y; j<y+3 ; j++) {
				board[i][j] = (board[i][j]==0?1:0);
			}
		}
	}

}
