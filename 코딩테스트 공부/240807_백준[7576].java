import java.util.*;
import java.io.*;

// bfs/토마토/g5

public class Main {
	
	public static int[] dx = {-1,0,1,0};//위,오,아래,왼
	public static int[] dy = {0,1,0,-1};
	public static StringTokenizer st;
	public static int[][] tomato;
	public static Queue<int[]> que = new LinkedList<>();
	public static int x,y,mx,my,ans;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine()," ");
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		
		//토마토 박스 입력받기
		tomato = new int[m][n]; //0으로 초기화됨
	
		for(int i=0;i<m;i++) {
			st = new StringTokenizer(br.readLine()," ");
			for(int j=0;j<n;j++) {
				int tmp = Integer.parseInt(st.nextToken());
				tomato[i][j]=tmp;
				if (tmp==1) que.add(new int[] {i,j}); //큐에 넣기_bfs를 위함
			}
		}
//		System.out.println(que);
		
		//bfs
		while(!que.isEmpty()) {
			int[] loca = que.poll();
			x=loca[0];
			y=loca[1];
			
			for(int i=0;i<4;i++) {
				mx=x+dx[i];
				my=y+dy[i];
				
				if (0<=mx && mx<m && 0<= my && my<n && tomato[mx][my]==0) {
					tomato[mx][my] = tomato[x][y]+1;
					que.add(new int[] {mx,my});
				}
			}
		}
		
		ans = 0;
		for(int i=0;i<m;i++) {
			for (int j=0;j<n;j++) {
				if(tomato[i][j]==0) {
					System.out.println(-1);
					return;
				}
				ans = Math.max(tomato[i][j], ans);
			}
		}
		
		System.out.println(ans-1);

	}

}
