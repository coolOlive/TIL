package com.baekjoon2;

// 유니온파인드/그래프이론/거짓말/골드4

import java.io.*;
import java.util.*;

public class Main_1043 {
	static StringTokenizer st;
	static int n,m,knowPcnt,ans=0;
	static ArrayList<Integer>[] party; //인접리스트
	static boolean[] iknow;
	static int[] parent;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		// 초기화
		party = new ArrayList[m];
		parent = new int[n+1];
		iknow = new boolean[n+1];
		
		for(int i=0;i<n+1;i++) {
			parent[i] = i;
		}
		
		for(int i=0;i<m;i++) {
			party[i] = new ArrayList<>();
		}
		
		st = new StringTokenizer(br.readLine());
		knowPcnt = Integer.parseInt(st.nextToken());
		for(int i=0;i<knowPcnt ; i++) {
			int tmp = Integer.parseInt(st.nextToken());
			iknow[tmp] = true;
		}
		

		//파티 입력받기
		for(int i=0;i<m;i++) {
			st = new StringTokenizer(br.readLine());
			int tmp = Integer.parseInt(st.nextToken());
			if(tmp!=0) {
				int p = Integer.parseInt(st.nextToken());
				party[i].add(p);
				
				for(int j=1;j<tmp;j++) {
					int pp = Integer.parseInt(st.nextToken());
					union(p,pp);
					party[i].add(pp);
				}
			}
			
		}
		
		//진실 아는 그룹 찾기_진실 말하기
		findtrueGroup();
		
		//거짓말 가능한 그룹_정답 그룹
		findfalseGroup();
		
		System.out.println(ans);

	}
	
	static void findfalseGroup() {
		for(ArrayList<Integer> par:party) {
			boolean canlie = true;
			for(int p:par) {
				if(iknow[find(p)]) {
					canlie=false;
					break;
				}
			}
			if (canlie) ans++;
		}
	}
	
	static void findtrueGroup() {
		for (int i=1;i<n+1;i++) {
			if(iknow[i]) {
				for(int j=1;j<n+1;j++) {
					if(find(j)==find(i)) iknow[j] = true;
				}
			}
		}
	}
	
	static int find(int x) {
		if(parent[x]==x) return x;
		return parent[x]=find(parent[x]);
	}
	
	static void union(int a, int b) {
		int p1 = find(a);
		int p2 = find(b);
		if(p1!=p2) parent[p2] = p1;
	}

}
