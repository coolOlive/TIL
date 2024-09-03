// 플로이드워셜/케빈 베이컨의 6단계 법칙/실버1

import java.io.*;
import java.util.*;

public class Main {
	static final int INF = Integer.MAX_VALUE/2;
	static StringTokenizer st;
	static int n, m,minline=Integer.MAX_VALUE,minnum;
	static int[][] board;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		// 초기화_inf
		board = new int[n + 1][n + 1];
		minnum = n+1;
		for(int i=0;i<n+1;i++) {
			for(int j=0;j<n+1;j++) {
				board[i][j] = INF;
				if(i==j) board[i][j] = 0;
			}
		}

		// 입력받기
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			board[a][b] = 1;
			board[b][a] = 1;
		}
		
		// 플로이드 워셜로 해야함_ 다익스트라로 한 정점에서 다른 정점까지 계산하면 걍 장난없음
		// 모든 정점에서 모든 정점으로 가는 거리 계산하는 알고(음수x,사이클x)
		// dp랑 인접행렬 사용

		// 최단경로 초기화_모든 정점 k에대해 i->j로 가는 거리 갱신
		for (int k = 0; k < n + 1; k++) {
			for (int i = 0; i < n + 1; i++) {
				for (int j = 0; j < n + 1; j++) {
					if (board[i][k] + board[k][j] < board[i][j]) {
						board[i][j] = board[i][k] + board[k][j];
                    }
				}
			}
		}
		
		for(int i=1;i<n+1;i++) {
			int cnt = 0;
			for(int j=1;j<n+1;j++) {
				cnt+= board[i][j];
			}
			
			if(minline>cnt) {
				minline = cnt;
				minnum = i;
			}
		}
		
		System.out.println(minnum);
	}

}



