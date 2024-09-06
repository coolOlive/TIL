package com.baekjoon2;

// bfs/헌내기는 친구가 필요해/실버2

import java.io.*;
import java.util.*;

public class Main_21736 {
	static char[][] board;
	static int[] dx = {-1,0,1,0};//상우하좌
	static int[] dy = {0,1,0,-1};
	static int n,m,x,y,ans=0;
	static boolean[][] visit;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		
		//초기화
		board = new char[n][m];
		visit = new boolean[n][m];
		
		for(int i=0;i<n;i++) {
			String tmp = sc.next();
			for(int j=0;j<m;j++) {
				board[i][j] = tmp.charAt(j);
				if(board[i][j]=='I') { //도연위치
					x = i;
					y = j;
				}
			}
		}
		
		
		bfs();
		
		if(ans>0)System.out.println(ans);
		else System.out.println("TT");
	}
	
	static void bfs() {
		Queue<int[]> que = new ArrayDeque<>();
		
		que.add(new int[] {x,y});
		visit[x][y] = true;
		
		while(!que.isEmpty()) {
			int[] now = que.poll();
			int nx = now[0];
			int ny = now[1];
			
			for(int i=0;i<4;i++) {
				int mx = nx+dx[i];
				int my = ny+dy[i];
				
				if(rangeCheck(mx, my) && !visit[mx][my]) {
					if(board[mx][my]=='P') ans++;
					if(board[mx][my]!='X') {
						visit[mx][my] = true;
						que.offer(new int[] {mx,my});
					}
				}
				
			}
		}
		
	}
	
	static boolean rangeCheck(int a, int b) {
		return (a>=0&&a<n&&b>=0&&b<m);
	}

}
