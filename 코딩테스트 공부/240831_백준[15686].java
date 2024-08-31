import java.io.*;
import java.util.*;

// 백트래킹,구현,브루트포스/치킨 배달/골드5

class Loca {
    int x;
    int y;
    
    Loca(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class JUN15686_ChickenDelivery_박유진 {
	static StringTokenizer st;
	static int n,m;
    static int[][] board;
    static boolean[] visited;
    static List<Loca> houses = new ArrayList<>();
    static List<Loca> chickens = new ArrayList<>();
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        //초기화
        board = new int[n][n];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                
                if(board[i][j] == 1) houses.add(new Loca(i,j));//집
                else if(board[i][j] == 2) chickens.add(new Loca(i,j));//치킨
            }
        }

        //치킨집 방문 초기화
        visited = new boolean[chickens.size()];
        
        dfs(0, 0);
        
        System.out.println(ans);
    }

    //거리계산_dfs
    static void dfs(int idx,int cnt) {
        if(cnt==m) {
            int cityDist = 0; //도시 전체 키친거리

            for(Loca h : houses) {
                int homeDist = Integer.MAX_VALUE; //각자 집에서 제일 가까운 치킨집 거리
                
                for(int i=0; i<chickens.size(); i++) { //현재 위치에서 모든 치킨집 돌며 검사하고 제일 작은거 찾기
                    if(visited[i]) {
                        int dist = Math.abs(h.x-chickens.get(i).x) + Math.abs(h.y-chickens.get(i).y);
                        homeDist = Math.min(homeDist, dist);
                    }
                }
                cityDist+= homeDist;
            }

            ans = Math.min(ans,cityDist);
            return;
        }

        for(int i=idx; i<chickens.size(); i++) {
            visited[i] = true;
            dfs(i+1, cnt+1); //다음 치킨집 선택
            visited[i] = false;
        }
    }

    
}
