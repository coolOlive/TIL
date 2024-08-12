package com.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// dp,수학/합분해/골드5

public class Main_2225 {
	static int n,k;
	static int[] dp;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		dp = new int[n+1];
		Arrays.fill(dp, 1); //1로 초기화
		
		for(int i=2;i<k+1;i++) {
			for (int j=1;j<n+1;j++) {
				dp[j] = (dp[j]+dp[j-1])%1000000000;
//				System.out.println(Arrays.toString(dp));
			}
			
		}
//		System.out.println(Arrays.toString(dp));
		System.out.println(dp[n]);
		
	}


}

