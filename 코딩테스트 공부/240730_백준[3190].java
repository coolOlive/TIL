import java.util.*;
import java.io.*;

// 구현,자료구조/뱀/골드4

public class Main_3190 {
    public static StringTokenizer st;
    public static int n, k, a, b, l, time;
    public static String direc;
    public static int[][] board;
    public static HashMap<Integer, String> move = new HashMap<>();
    public static LinkedList<int[]> snake = new LinkedList<>();
    public static int[] dx = {0, 1, 0, -1};
    public static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        board = new int[n][n];
        
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            board[a - 1][b - 1] = 1;
        }
        
        l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            time = Integer.parseInt(st.nextToken());
            direc = st.nextToken();
            move.put(time, direc);
        }
        
        snakeMove();
    }

    static void snakeMove() {
        int ans = 0;
        int d = 0;
        int x = 0, y = 0;
        snake.add(new int[]{0, 0});
        
        while (true) {
            ans++;
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || ny < 0 || nx >= n || ny >= n) break; // 벽에 부딪힘
            
            for (int[] part : snake) {
                if (nx == part[0] && ny == part[1]) {
                    System.out.println(ans); // 자기 몸에 부딪힘
                    return;
                }
            }
            
            if (board[nx][ny] == 1) { // 사과가 있는 경우
                board[nx][ny] = 0;
                snake.add(new int[]{nx, ny});
            } else { // 사과가 없는 경우
                snake.add(new int[]{nx, ny});
                snake.poll(); // 꼬리 제거
            }
            
            if (move.containsKey(ans)) {
                if (move.get(ans).equals("L")) {
                    d = (d + 3) % 4; // 왼쪽 회전
                } else {
                    d = (d + 1) % 4; // 오른쪽 회전
                }
            }
            
            x = nx;
            y = ny;
        }
        System.out.println(ans);
    }
}
