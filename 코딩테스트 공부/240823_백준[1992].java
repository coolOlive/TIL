package com.baekjoon;

import java.util.*;

// 부분집합,재귀/쿼드트리/실버1

public class JUN1992_QuadTree_박유진 {
	static int n;
	static int[][] board;
	static String ans = "";

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		board = new int[n][n];
		
		for(int i=0;i<n;i++) {
			String[] tmp = sc.next().split("");
			for(int j=0;j<n;j++) {
				board[i][j] = Integer.parseInt(tmp[j]);
			}
		}
		
		makeQuad(0,0,n);
		System.out.println(ans);

	}
	
	static void makeQuad(int x, int y, int len) {
		if(checkBox(x,y,len)) {
			ans+=(board[x][y]+"");
		} else {
			int divLen = len/2;
			ans+="(";
			
			makeQuad(x, y, divLen);
			makeQuad(x, y+divLen, divLen);
			makeQuad(x+divLen, y, divLen);
			makeQuad(x+divLen, y+divLen, divLen);
			
			ans+=")";
		}
	}
	
	
	// 범위 안의 값 같은지 체크
	static boolean checkBox(int x,int y,int len) {
		int cell = board[x][y];
		
		for(int i=x;i<x+len;i++) {
			for(int j=y;j<y+len;j++) {
				if(cell!=board[i][j]) return false;
			}
		}
		
		return true;
	}

}
