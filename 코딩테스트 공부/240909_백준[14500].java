package com.baekjoon2;

// dfs/테트로미노/골드4

import java.io.*;
import java.util.*;

public class Main_14500 {
    static int[][] board;
    static boolean[][] visit;
    static int n, m, max = Integer.MIN_VALUE;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        visit = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visit[i][j] = true;
                dfs(i, j, 1, board[i][j]);
                visit[i][j] = false;
                special(i, j); // ㅗ 모양은 따로 처리
            }
        }

        System.out.println(max);
    }

    static void dfs(int x, int y, int depth, int sum) {
        if (depth == 4) {
            max = Math.max(max, sum);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < n && ny < m && !visit[nx][ny]) {
                visit[nx][ny] = true;
                dfs(nx, ny, depth + 1, sum + board[nx][ny]);
                visit[nx][ny] = false;
            }
        }
    }

    // ㅗ 모양 테트로미노 처리
    static void special(int x, int y) {
        int[][] shapes = {
            {0, 1, 0, -1, -1, 0}, // ㅗ
            {0, 1, 0, -1, 1, 0},  // ㅜ
            {1, 0, -1, 0, 0, -1}, // ㅓ
            {1, 0, -1, 0, 0, 1}   // ㅏ
        };

        for (int i = 0; i < 4; i++) {
            int sum = board[x][y];
            boolean valid = true;

            for (int j = 0; j < 3; j++) {
                int nx = x + shapes[i][j * 2];
                int ny = y + shapes[i][j * 2 + 1];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                    valid = false;
                    break;
                }

                sum += board[nx][ny];
            }

            if (valid) {
                max = Math.max(max, sum);
            }
        }
    }
}
