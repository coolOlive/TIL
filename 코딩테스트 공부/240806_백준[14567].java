import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// dp,위상정렬/선수과목 (Prerequisite)/g5

public class Main {
    static int n, m;
    static int[] order, ans;
    static List<List<Integer>> subj = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        /* 입력 부분 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken()); // 과목의 수
        m = Integer.parseInt(st.nextToken()); // 선수 관계의 수

        order = new int[n+1]; // 진입 차수 배열
        ans = new int[n+1]; // 수강 가능 학기 저장 배열

        for(int i = 0; i < n+1; i++) {
            subj.add(new ArrayList<>());
        }
        
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            order[b]++; // 후속 과목의 진입 차수 증가
            subj.get(a).add(b); // 선수 과목 a가 후속 과목 b를 가리키도록 그래프에 추가
        }
        
        /* 로직 */
        Queue<int[]> que = new ArrayDeque<>();
        
        for (int i = 1; i <= n; i++) { // 전체 과목을 순회하며 초기 진입 차수가 0인 과목을 큐에 넣고 해당 학기 기록
            if (order[i] == 0) {
                que.add(new int[] {i, 1});
                ans[i] = 1; // 수강 가능 학기를 1로 설정
            }
        }
        
        while(!que.isEmpty()) {
            int[] nowSubj = que.poll(); // 현재 과목
            
            for(int su : subj.get(nowSubj[0])) { // 현재 과목의 후속 과목의 진입 차수 감소
                order[su]--;
                
                if(order[su] == 0) { // 진입 차수가 0이 되면 수강 가능
                    ans[su] = nowSubj[1] + 1; // 다음 학기부터 수강 가능하므로 +1
                    que.add(new int[] {su, nowSubj[1] + 1}); // 후속 과목을 큐에 추가
                }
            }
        }
        
        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i <= n; i++) {
            sb.append(ans[i]).append(" ");
        }
        System.out.println(sb);
    }
}
