package com.baekjoon;

import java.io.*;
import java.util.*;

// bfs/치즈/골드4

public class JUN2636_Cheese_박유진 {
	static int n,m,eachCheese,totalTime,totalCheese,ansCheeseCnt;
	static StringTokenizer st;
	static int[][] board;
	static boolean[][] visit;
	static int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}}; //상우하좌

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		//초기화
		board = new int[n][m];
		totalTime = 0;
		
		//보드 입력받기
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<m;j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				
				if(board[i][j]==1) totalCheese++;
			}
		}
		
		while(totalCheese>0) {
			visit = new boolean[n][m];
			eachCheese = 0;
			ansCheeseCnt = totalCheese;
			
			// 덩어리 개수 count_bfs
			for(int i=0;i<n;i++) {
				for(int j=0;j<m;j++) {
					if(!visit[i][j] && board[i][j]==1) {
						bfs(i,j);
						
					}
				}
			}
			
			visit = new boolean[n][m];
			
			//가장자리 치즈 줄이기
			noCheese(0,0);
			
			
			//시간++
			totalTime++;
		}
		
		//정답 출력 부분
		System.out.println(totalTime);
		System.out.println(ansCheeseCnt);
		

	}//main end
	
	static void noCheese(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visit[x][y] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int nx = now[0];
            int ny = now[1];

            for (int i=0; i<4; i++) {
                int mx = nx+dir[i][0];
                int my = ny+dir[i][1];

                if (rangeCheck(mx,my) && !visit[mx][my]) {
                    visit[mx][my] = true;
                    if (board[mx][my] == 1) {
                        // 치즈가 녹음
                        board[mx][my] = 0;
                        eachCheese++;
                        totalCheese--;
                    } else {
                        queue.offer(new int[]{mx,my});
                    }
                }
            }
        }
	}
	
	
	static void bfs(int x, int y) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {x,y});
		visit[x][y] = true;
		
		while(!queue.isEmpty()) {
			int[] now = queue.poll();
			int nx = now[0];
			int ny = now[1];
			for(int i=0;i<4;i++) {
				int mx = nx+dir[i][0];
				int my = ny+dir[i][1];
				
				if(rangeCheck(mx, my) && !visit[mx][my] && board[mx][my]==1) {
					queue.offer(new int[] {mx,my});
					visit[mx][my] = true;
					eachCheese++;
				}
			}
		}
	}
	
	static boolean rangeCheck(int x,int y) {
		return (x>=0 && x<n && y>=0 && y<m);
	}

}
