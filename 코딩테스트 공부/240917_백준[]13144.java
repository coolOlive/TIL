package com.baekjoon2;

// 투포인터/List of Unique Numbers/골드4

import java.io.*;
import java.util.*;

public class Main_13144 {
	static StringTokenizer st;
	static int n, start = 0, end = 0;
	static long ans = 0;
	static int[] nums;
	static boolean[] samecheck;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());

		// 초기화
		nums = new int[n];
		samecheck = new boolean[100001];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}

		while (end < n) {

			if (!samecheck[nums[end]]) {
				samecheck[nums[end]] = true;
				ans += end - start + 1;
				end++;
			} else {
				samecheck[nums[start]] = false;
				start++;
			}

		}
		System.out.println(ans);

	}
}
