import java.util.*;
import java.io.*;

// 자료구조/파일 합치기 3/G4
//K ≤ 1,000,000 -> 자료형 int로 부족

public class Main_13975 {
	
	public static int T,k;
	public static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		T = Integer.parseInt(br.readLine());
		
		for (int tc=0;tc<T;tc++) {
			k = Integer.parseInt(br.readLine());
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			//파일크기 넣을 배열
			PriorityQueue<Long> files = new PriorityQueue<>();
			
			for(int i=0;i<k;i++) {
				files.add(Long.parseLong(st.nextToken()));
			}
//			System.out.println(files+"---");
			long ans = 0;
			
			while (files.size()>1) {
				long tmp = files.poll()+files.poll();
				ans += tmp;
				
				files.add(tmp);
			}
			
//			System.out.println(files);
			System.out.println(ans);
		}

	}

}
