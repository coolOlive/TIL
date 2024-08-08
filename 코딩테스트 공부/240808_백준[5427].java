package com.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// 그래프탐색,너비우선탐색/불/골드4

public class Main_5427 {
    static int T, w, h, startX, startY, nx, ny, ans;
    static StringTokenizer st;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static char[][] building;
    static int[] dx = {-1, 0, 1, 0}; // 상우하좌
    static int[] dy = {0, 1, 0, -1};
    static Queue<int[]> fire;
    static Queue<int[]> person;
    static boolean escapeFlg;

    public static void main(String[] args) throws NumberFormatException, IOException {
        T = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < T; tc++) {
            inputs();
            escapeFlg = false; // 탈출 플래그 초기화
            ans = -1;
            escape();

            if (escapeFlg) System.out.println(ans);
            else System.out.println("IMPOSSIBLE");
        }
    }

    public static void escape() {
        int time = 0;

        while (!person.isEmpty()) {
            time++;
            burning(); // 먼저 불을 퍼뜨린다.

            int personCount = person.size();
            for (int i = 0; i < personCount; i++) {
                int[] now = person.poll();

                for (int j = 0; j < 4; j++) {
                    int a = now[0] + dx[j];
                    int b = now[1] + dy[j];

                    // 탈출 성공 로직
                    if (a < 0 || a >= h || b < 0 || b >= w) {
                        escapeFlg = true;
                        ans = time;
                        return;
                    }

                    // 접근 가능한 곳으로 이동
                    if (building[a][b] == '.') {
                        person.offer(new int[]{a, b});
                        building[a][b] = '@'; // 방문 처리
                    }
                }
            }
        }
    }

    public static void burning() {
        int fireCount = fire.size();
        for (int i = 0; i < fireCount; i++) {
            int[] fireLoca = fire.poll();

            for (int j = 0; j < 4; j++) {
                nx = fireLoca[0] + dx[j];
                ny = fireLoca[1] + dy[j];
                if (nx >= 0 && nx < h && ny >= 0 && ny < w && building[nx][ny] == '.') {
                    building[nx][ny] = '*';
                    fire.offer(new int[]{nx, ny});
                }
            }
        }
    }

    public static void inputs() throws NumberFormatException, IOException {
        st = new StringTokenizer(br.readLine());
        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        building = new char[h][w];
        fire = new LinkedList<>();
        person = new LinkedList<>();

        for (int i = 0; i < h; i++) {
            String one = br.readLine();
            for (int j = 0; j < w; j++) {
                char tmp = one.charAt(j);

                if (tmp == '@') {
                    startX = i;
                    startY = j;
                    building[i][j] = '.';
                    person.offer(new int[]{i, j});
                } else if (tmp == '*') {
                    fire.offer(new int[]{i, j});
                }
                building[i][j] = tmp;
            }
        }
    }
}
