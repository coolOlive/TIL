package com.baekjoon2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 정렬/Sport Climbing Combined/실버5

class Score implements Comparable<Score> {
	int player, a, b, c;
	int mulScore, hapScore;

	public Score(int player, int a, int b, int c) {
		super();
		this.player = player;
		this.a = a;
		this.b = b;
		this.c = c;
		this.mulScore = a * b * c;
		this.hapScore = a + b + c;
	}

	@Override
	public int compareTo(Score o) {
		if (this.mulScore != o.mulScore)
			return Integer.compare(this.mulScore, o.mulScore);
		if (this.hapScore != o.hapScore)
			return Integer.compare(this.hapScore, o.hapScore);
		return Integer.compare(this.player, o.player);
	}

	@Override
	public String toString() {
		return "Score [player=" + player + ", a=" + a + ", b=" + b + ", c=" + c + ", mulScore=" + mulScore
				+ ", hapScore=" + hapScore + "]";
	}

}

public class Main_23246 {
	static StringTokenizer st;
	static int n;
	static PriorityQueue<Score> info = new PriorityQueue<>();
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());

		for (int i = 0; i < n; i++) {
			inputs(br, i);
		}
		
		for(int i=0;i<2;i++) {
			sb.append(info.poll().player).append(" ");
		}
		sb.append(info.poll().player);
		System.out.println(sb);

	}

	static void inputs(BufferedReader br, int idx) throws IOException {
		st = new StringTokenizer(br.readLine());
		int player = Integer.parseInt(st.nextToken());
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		info.offer(new Score(player, a, b, c));

	}

}
