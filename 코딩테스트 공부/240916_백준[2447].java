package com.baekjoon2;

// 재귀,분할정복/별 찍기 - 10/골드5

import java.util.*;

public class Main_2447 {
	static int n;
	static char[][] board;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();

		// 초기화
		board = new char[n][n];
		for (int i = 0; i < n; i++) {
			Arrays.fill(board[i], '*');
		}

		// 재귀 돌리기
		makeBoard(0, 0, n);

		for (int i = 0; i < n; i++) {
			System.out.println(board[i]);
		}

	}

	static void makeBoard(int x, int y, int size) {
		// 기저조건
		if (size == 1)
			return;

		// 블록 만들기
		int eachLen = size / 3;

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (i == 1 && j == 1) {
					// 공백 만들기
					makeBlank(x + i * eachLen, y + j * eachLen, eachLen);
				} else {
					// 블록 만들기
					makeBoard(x + i * eachLen, y + j * eachLen, eachLen);
				}
			}
		}

	}

	static void makeBlank(int x, int y, int size) {
		for (int i = x; i < x + size; i++) {
			for (int j = y; j < y + size; j++) {
				board[i][j] = ' ';
			}
		}
	}

}
