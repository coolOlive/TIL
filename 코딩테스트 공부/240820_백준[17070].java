package com.baekjoon;

import java.io.*;
import java.util.*;

// dp,그래프이론,그래프탐색/파이프 옮기기 1/골드5

public class Main_17070 {
	static int n, ans=0,mx,my;
	static StringTokenizer st;
	static int[][] board;
	static int[] dx = {0,1,1};//가로,세로,대각
	static int[] dy = {1,0,1};

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		board = new int[n][n];
		
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<n;j++) {
				board[i][j]=Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0,1,0); //0가로1세로2대각
		System.out.println(ans);

	}
	
	static void dfs(int x,int y,int dir) {
		if (x==(n-1) && y==(n-1)) { //목표지점
			ans++;
			return;
		}
		
		for(int i=0;i<3;i++) {
			if (dir==0 && i==1) continue; //가로일때는 세로 안됨
			if (dir==1&& i==0) continue; //세로일때는 가로 안됨
			
			mx = x+dx[i];
			my = y+dy[i];
			
			if(mx>=0 && mx<n && my>=0 && my<n) {
				if (i==2) { //대각선일때는 3곳이 다 비어야함
					if (board[mx][my] == 0 && board[x + 1][y] == 0 && board[x][y + 1] == 0) {
                        dfs(mx, my, i);
                    }
                } else { //가로세로는 그 칸만 비면 됨
                    if (board[mx][my] == 0) {
                        dfs(mx, my, i);
                    }
                }
			}
			
		}
		
	}

}
