import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

// dfs,bfs/DFS와 BFS/실버2

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputs = br.readLine().split(" ");
		int n = Integer.parseInt(inputs[0]), m = Integer.parseInt(inputs[1]), v = Integer.parseInt(inputs[2]);
		int[][] graph = new int[n+1][n+1];
		boolean[] visit =  new boolean[n+1];
		
		for (int i = 0;i<m;i++) {
			String[] xy = br.readLine().split(" ");
			int x = Integer.parseInt(xy[0]);
			int y = Integer.parseInt(xy[1]);
			graph[x][y] = 1;
			graph[y][x] = 1;
		}
		dfs(v,graph,visit);
		System.out.println();
		Arrays.fill(visit, false);
		bfs(v,graph,visit);

	}
	
	public static void dfs(int v, int[][] graph, boolean[] visit) {
		visit[v] = true;
		System.out.print(v+" ");
		
		for(int i = 1;i<graph.length;i++) {
			if (graph[v][i]==1 && !visit[i]) {
				dfs(i,graph,visit);
			}
		}
	}
	
	public static void bfs(int v, int[][] graph, boolean[] visit) {
		Queue<Integer> que = new LinkedList<>();
		que.add(v);
		visit[v] = true;
		
		while (!que.isEmpty()) {
			int next = que.poll();
			System.out.print(next+" ");
			
			for (int i = 1;i<graph[next].length;i++) {
				if(graph[next][i]==1 && !visit[i]) {
					visit[i] = true;
					que.add(i);
				}
			}
		}
	}

}
