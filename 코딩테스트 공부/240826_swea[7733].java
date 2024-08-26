package com.swea;

import java.util.*;
import java.io.*;

// bfs/치즈 도둑/d4

public class SW7733_CheeseThief_박유진 {
	static int T,n, ans,eachDayCnt,maxDay;
	static StringTokenizer st;
	static int[][] board;
	static boolean[][] visit;
	static int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}}; //상우하좌

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for(int tc=1;tc<=T; tc++) {
			n = Integer.parseInt(br.readLine());
			
			//값 초기화
			board = new int[n][n];
			maxDay = 1;
			ans = 0; //치즈 덩어리 수
			
			//입력받기
			for(int i=0;i<n;i++) {
				st = new StringTokenizer(br.readLine());
				for(int j=0;j<n;j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
					maxDay = Math.max(maxDay, board[i][j]);
				}
				
			}
			
			//날짜 돌기
			for(int i=0;i<=maxDay;i++) {
				visit = new boolean[n][n];
				eachDayCnt = 0;
				
				for(int j=0;j<n;j++) {
					for(int k=0;k<n;k++) {
						if(board[j][k]>i && !visit[j][k]) {
							bfs(j,k,i);
							eachDayCnt++;
//							System.out.println(j+" "+k+" "+eachDayCnt);
						}
					}
				}
				
				ans = Math.max(ans,eachDayCnt);
				
			}
			System.out.println("#"+tc+" "+ans);
			
		} //tc for end

	}
	
	static void bfs(int x, int y,int day) {
		Queue<int[]> que = new LinkedList<>();
		que.add(new int[]{x, y});
		visit[x][y] = true;
		
		while(!que.isEmpty()) {
			int[] now = que.poll();
			int nx = now[0];
			int ny = now[1];
			
			for(int i=0;i<4;i++) {
				int mx = nx+dir[i][0];
				int my = ny+dir[i][1];
				
				if(checkRange(mx,my) && !visit[mx][my] && board[mx][my]>day) {
					visit[mx][my] = true;
					que.offer(new int[] {mx,my});
				}
				
			}
		}
		
	}
	
	static boolean checkRange(int x, int y) {
		return (x>=0&& x<n && y>=0 && y<n);
	}

}
