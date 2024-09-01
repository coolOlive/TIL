import java.util.*;
import java.io.*;

// 그래프이론,bfs,dfs/게리맨더링/골드3

public class Main {
	static StringTokenizer st;
	static int n, pnums[],totalP , ans = Integer.MAX_VALUE;
	static boolean[] visit, bfsVisit;
	static ArrayList<Integer>[] part;
	

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		
		//구역별 사람 수
		pnums = new int[n];
		totalP = 0;
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++) {
			pnums[i] = Integer.parseInt(st.nextToken());
			totalP += pnums[i];
		}
		
		//연결관계 입력
		part = new ArrayList[n]; //인접리스트
		for(int i=0;i<n;i++) {
			part[i] = new ArrayList<Integer>();
		}
		
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			int pcnt = Integer.parseInt(st.nextToken());
			for(int j=0;j<pcnt ; j++) {
				part[i].add(Integer.parseInt(st.nextToken())-1);
			}
		}
		
//		for(int i=0;i<n;i++) {
//			System.out.println(part[i]);
//		}
		
		//부분집합 만들기(2개로 나누기)
		visit = new boolean[n];
		divP(0);
		
		if(ans==Integer.MAX_VALUE) System.out.println(-1);
		else System.out.println(ans);
		
	}
	
	//부분집합
	static void divP(int cnt) {
		if(cnt>=n) {
			//같은 구역인지 확인하기 _ 인구 수 cnt같이
			List<Integer> group1 = new ArrayList<>();
			List<Integer> group2 = new ArrayList<>();
			
			for(int i=0;i<n; i++) {
				if(visit[i]) group1.add(i);
				else group2.add(i);
			}
			
//			System.out.println(group1);
			
			if(checkConnect(group1)&& checkConnect(group2)) {
				calDiff(group1);
			}
			
			
//			System.out.println(cnt);
//			System.out.println(Arrays.toString(visit));
			return;
		}
		
		visit[cnt]=true;
		divP(cnt+1);
		visit[cnt] = false;
		divP(cnt +1);
		
	}
	
	static boolean checkConnect(List<Integer> list) {
		//모두 같은거면
		if(list.size()==n || list.size()==0) return false;
		
		Queue<Integer> que = new ArrayDeque<>();
		bfsVisit = new boolean[n];
		int cnt=1;
		
		que.add(list.get(0));
		bfsVisit[list.get(0)] = true;
		
		while (!que.isEmpty()) {
			int now = que.poll();
			
			for(int next : part[now]) {
				if(list.contains(next) &&  !bfsVisit[next]) {
					que.offer(next);
					bfsVisit[next] = true;
					cnt++;
				}
			}
			
		}
//		System.out.println(cnt);
		return list.size()==cnt;
		
	}
	
	//인구 수 계산
	static void calDiff(List<Integer> list) {
		int g1 = 0, g2 = 0;
		
		for(int pnum:list) {
			g1+= pnums[pnum];
		}
		
		g2 = totalP-g1;
		ans = Math.min(ans, Math.abs(g1-g2));
		
	}

}
