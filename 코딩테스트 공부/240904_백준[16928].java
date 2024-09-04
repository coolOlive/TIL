import java.io.*;
import java.util.*;

// bfs/뱀과 사다리 게임/골드5

public class Main_16928 {
	static StringTokenizer st;
	static int n, m;
	static int[] board, dist;
	static boolean[] visit;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		inputs(br);
		bfs();
		System.out.println(dist[99]);

	}

	static void bfs() {
		Queue<Integer> que = new LinkedList<Integer>();
		visit[0] = true;
		que.add(0);

		while (!que.isEmpty()) {
//			System.out.println(que);

			int now = que.poll();

			for (int i = 1; i < 7; i++) {
				int next = now + i;

				if (next >= 100)
					continue;
				next = board[next];

				if (!visit[next]) {
					visit[next] = true;
					dist[next] = dist[now] + 1;
					que.add(next);

				}
			}

		}

	}

	static void inputs(BufferedReader br) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		// 초기화
		board = new int[100];
		dist = new int[100];
		visit = new boolean[100];

		for (int i = 0; i < 100; i++) {
			board[i] = i;
		}

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			board[from - 1] = to - 1;
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			board[from - 1] = to - 1;
		}

	}

}
