package com.baekjoon2;

// bfs/토마토/골드5

import java.io.*;
import java.util.*;

class Loca {
    int z, y, x;
    Loca(int z, int y, int x) {
        this.z = z;
        this.y = y;
        this.x = x;
    }
}

public class Main_7569 {
    //상우하좌아래위
	static int[] dx = {-1,0,1,0,0,0};
	static int[] dy = {0,1,0,-1,0,0};
	static int[] dz = {0,0,0,0,1,-1};
    static int m, n, h,maxDay=0;
    static int[][][] box;
    static Queue<Loca> que;  //익은 토마토 위치
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        //초기화
        box = new int[h][n][m];
        que = new LinkedList<>();

        //입력 받기
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    box[i][j][k] = Integer.parseInt(st.nextToken());
                    // 익은 토마토면 큐에 추가
                    if (box[i][j][k] == 1) {
                        que.add(new Loca(i, j, k));
                    }
                }
            }
        }
        
        System.out.println(bfs());
    }

    static int bfs() {
        while (!que.isEmpty()) {
            Loca point = que.poll();
            int z = point.z;
            int y = point.y;
            int x = point.x;

            for (int i = 0; i < 6; i++) {
                int nz = z + dz[i];
                int ny = y + dy[i];
                int nx = x + dx[i];

                // 범위 내, 안 익은거면 익게 처리
                if (rangeCheck(nx,ny,nz)) {
                    if (box[nz][ny][nx] == 0) {
                        que.add(new Loca(nz, ny, nx));
                        box[nz][ny][nx] = box[z][y][x] + 1; //시간더하기
                    }
                }
            }
        }

        //계산하기
        for (int i=0;i<h;i++) {
            for (int j=0;j<n;j++) {
                for (int k=0;k<m;k++) {
                	//안익은거 있을 때
                    if (box[i][j][k] == 0) return -1;
                    maxDay = Math.max(maxDay, box[i][j][k]);
                }
            }
        }

        if (maxDay == 1) return 0;
        
        return maxDay-1;
    }
    
    static boolean rangeCheck(int x, int y, int z) {
        return (x >= 0 && x < m && y >= 0 && y < n && z >= 0 && z < h);
    }

}
