package com.baekjoon;

import java.io.*;
import java.util.*;

// 정렬,스위핑/선 긋기/골드5

class Pair implements Comparable<Pair>{
	int start;
	int end;
	
	public Pair(int start, int end) {
		super();
		this.start = start;
		this.end = end;
	}

	@Override
	public int compareTo(Pair o) {
		if(this.start==o.start) {
			return this.end-o.end;
		}
		return this.start-o.start;
	}
}

public class Main_2170 {
	static int n,s,e,ans=0;
	static PriorityQueue<Pair> que = new PriorityQueue<>();
	static Pair[] lines;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		inputs();
		cntLength();
		System.out.println(ans);
	}
	
	public static void inputs() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		lines = new Pair[n];
		
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			s=Integer.parseInt(st.nextToken());
			e=Integer.parseInt(st.nextToken());
			
			lines[i] = new Pair(s, e);
		}
	}
	
	public static void cntLength() {
		//lines정렬
		Arrays.sort(lines);
		
		int nowS = lines[0].start;
		int nowE = lines[0].end;
		
		for(int i=1;i<n;i++) {
			if(lines[i].start>nowE) { //지금 선과 겹치지 않을 때
				ans += nowE-nowS;
				nowS = lines[i].start;
				nowE = lines[i].end;
			} else if(nowE<lines[i].end) { //겹칠 때
				nowE = lines[i].end;
			}
		}
		
		ans+=(nowE-nowS);
	}

}
