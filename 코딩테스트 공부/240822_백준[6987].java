package com.swea;

import java.io.*;
import java.util.*;

// 백트래킹,조합/월드컵/골드4

class Nation {
	int wincnt;
	int samecnt;
	int losecnt;
	
	public Nation(int wincnt, int samecnt, int losecnt) {
		super();
		this.wincnt = wincnt;
		this.samecnt = samecnt;
		this.losecnt = losecnt;
	}

	public int getWincnt() {
		return this.wincnt;
	}

	public int getSamecnt() {
		return this.samecnt;
	}

	public int getLosecnt() {
		return this.losecnt;
	}

	public void setWincnt(int wincnt) {
		this.wincnt += wincnt;
	}

	public void setSamecnt(int samecnt) {
		this.samecnt += samecnt;
	}

	public void setLosecnt(int losecnt) {
		this.losecnt += losecnt;
	}
	
	
	
}

public class JUN6987_WorldCup_박유진 {
	static StringTokenizer st;
	static ArrayList<int[]> allMatch = new ArrayList<>(); //경기의 모든 경우의 수(조합) 저장하는 배열
	static int[] eachMatch = new int[2]; //각 경기 조합 ㄱ계산에 활용
	static ArrayList<Nation> nationInfo;
	static int win, lose, same;
	static int[] nations = {0,1,2,3,4,5};
	static boolean[] isSelected = new boolean[6];
	static String ans = "", flg;

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//모든 조합 구해두기
		allCombi(0,0);
		
		//총 4게임 진행
		for(int i=0;i<4;i++) {
			//입력받기, 초기화
			st = new StringTokenizer(br.readLine());
			
			nationInfo = new ArrayList<>();
			flg = "0";
			
			for(int j=0;j<6;j++) {
				win = Integer.parseInt(st.nextToken());
				same = Integer.parseInt(st.nextToken());
				lose = Integer.parseInt(st.nextToken());
				nationInfo.add(new Nation(win, same, lose));
			}
			
			//백트래킹
			backtracking(0);
			ans+=(flg+" ");
			
		} //game for종료
		
		System.out.println(ans.substring(0,ans.length()-1));
		
	}
	
	//모든 조합 구하는 함수
	static void allCombi(int cnt, int start) {
		if(cnt==2) {
			allMatch.add(eachMatch.clone());
			return;
		}
		
		for (int i=start;i<6;i++) {
			eachMatch[cnt] = nations[i];
			allCombi(cnt+1, i+1);
		}
	}
	
	// 백트래킹 실행 함수
	static void backtracking(int cnt) {
		if(cnt==15) {
			if(nationInfo.stream().allMatch(n -> n.getWincnt()==0 && n.getSamecnt()==0 && n.getLosecnt()==0)) {
				flg = "1";
			}
			
			return; //재귀 종료
		}
		
		//비교하는 팀2개의 win,lose,same 비교를 위한 변수들
		int team1 = allMatch.get(cnt)[0];
		int team2 = allMatch.get(cnt)[1];
		
		int team1Win = nationInfo.get(team1).getWincnt();
		int team1Same = nationInfo.get(team1).getSamecnt();
		int team1Lose = nationInfo.get(team1).getLosecnt();
		
		int team2Win = nationInfo.get(team2).getWincnt();
		int team2Same = nationInfo.get(team2).getSamecnt();
		int team2Lose = nationInfo.get(team2).getLosecnt();
		
		//앞 팀 이김
		if(team1Win > 0 && team2Lose > 0) {
			nationInfo.get(team1).setWincnt(-1);
			nationInfo.get(team2).setLosecnt(-1);
			backtracking(cnt+1);
			nationInfo.get(team1).setWincnt(1);
			nationInfo.get(team2).setLosecnt(1);
		}
		
		
		//비김
		if(team1Same > 0 && team2Same > 0) {
			nationInfo.get(team1).setSamecnt(-1);
			nationInfo.get(team2).setSamecnt(-1);
			backtracking(cnt+1);
			nationInfo.get(team1).setSamecnt(1);
			nationInfo.get(team2).setSamecnt(1);
		}
		
		
		//앞 팀 짐
		if(team1Lose > 0 && team2Win > 0) {
			nationInfo.get(team1).setLosecnt(-1);
			nationInfo.get(team2).setWincnt(-1);
			backtracking(cnt+1);
			nationInfo.get(team1).setLosecnt(1);
			nationInfo.get(team2).setWincnt(1);
		}
		
	}

}

