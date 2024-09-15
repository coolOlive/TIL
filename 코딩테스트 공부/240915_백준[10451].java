package com.baekjoon2;

// 그래프이론/순열 사이클/실버3

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_10451 {
	static StringTokenizer st;
	static int T, n, nums[], parents[];
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			n = Integer.parseInt(br.readLine());
			nums = new int[n + 1];
			parents = new int[n + 1];
			visited = new boolean[n + 1];

			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= n; j++) {
				nums[j] = Integer.parseInt(st.nextToken());
				parents[j] = j;
			}

			int ans = 0;
			for (int j = 1; j <= n; j++) {
				if (!visited[j]) {
					findCycle(j);
					ans++;
				}
			}
			System.out.println(ans);
		}
	}

	static void findCycle(int start) {
		int now = start;
		while (!visited[now]) {
			visited[now] = true;
			union(now, nums[now]);
			now = nums[now];
		}
	}

	static int find(int x) {
		if (parents[x] == x) {
			return x;
		}
		return parents[x] = find(parents[x]);
	}

	static void union(int x, int y) {
		int p1 = find(x);
		int p2 = find(y);

		if (p1 != p2) {
			parents[p1] = p2;
		}
	}
}
