package com.baekjoon;

import java.io.*;
import java.util.*;

// 구현/배열 돌리기 1/골드5

public class JUN16926_RotatingArray_박유진 {
	static StringTokenizer st;
	static int n,m,r;
	static int[][] board;
	static int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}}; //우하좌상
	static int[][] ans;

	public static void main(String[] args) throws IOException {
		inputs();
		
		//r번만큼 회전 돌리기!
		for(int k=0;k<r;k++) {
			moveBoard();
			for (int i=0;i<n; i++) {
                for (int j=0; j<m;j++) {
                    board[i][j] = ans[i][j];
                }
            }
		}
		
		//행렬 모두 홀수일 때, 중앙에 가만히 있는 칸 넣기
		if(n%2!=0 && m%2!=0) {
			int mid = n/2;
			ans[mid][mid] = board[mid][mid];
		}
		
		//출력하기
		for (int i = 0; i<n; i++) {
            for (int j=0; j<m; j++) {
                System.out.print(ans[i][j]+" ");
            }
            System.out.println();
        }
	}
	
	//입력받는 함수
	static void inputs() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		
		board = new int[n][m];
		ans = new int[n][m];
		
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
	}
	
	//회전시키는 함수
	static void moveBoard() {
		int lineCnt = Math.min(n,m)/2;
		
		for (int i = 0; i < lineCnt; i++) {
			//모서리
            int startx = i;
            int endx =n-i-1;
            int starty = i;
            int endy = m - i-1;

            // 위쪽 가로 -> 왼쪽으로
            for (int j = starty; j < endy; j++) {
                ans[startx][j] = board[startx][j+1];
            }

            // 오른쪽 세로 -> 위쪽으로
            for (int j = startx; j < endx; j++) {
                ans[j][endy] = board[j+1][endy];
            }

            // 아래쪽 가로 -> 오른쪽으로
            for (int j = endy; j > starty; j--) {
                ans[endx][j] = board[endx][j-1];
            }

            // 왼쪽 세로줄 -> 아래쪽으로
            for (int j = endx; j > startx; j--) {
                ans[j][starty] = board[j-1][starty];
            }
		}
	}
	
}
