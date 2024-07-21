import java.util.*;
import java.io.*;

// 정렬/강의실/S5

class Lecture {
	int lNum;
	int startT;
	int finishT;
	
	public Lecture(int lNum, int startT, int finishT) {
		this.lNum = lNum;
		this.startT = startT;
		this.finishT = finishT;
	}

	@Override
	public String toString() {
		return "Lecture [lNum=" + lNum + ", startT=" + startT + ", finishT=" + finishT + "]";
	}
	
}

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		Lecture[] lectures = new Lecture[n];
		int[] nowend = new int[n]; // 현재 강의실 종료 시간 넣기
    int cnt = 0;
		
		for (int i = 0;i<n;i++) {
			String[] input = br.readLine().split(" ");
			lectures[i] = new Lecture(Integer.parseInt(input[0]),Integer.parseInt(input[1]),Integer.parseInt(input[2]));
		}
		
		// 시작시간 기준으로 정렬
		Arrays.sort(lectures, new Comparator<Lecture>() {
        @Override
        public int compare(Lecture l1, Lecture l2) {
        	if(l1.startT != l2.startT) {
        		return Integer.compare(l1.startT, l2.startT);
        	}
        	return Integer.compare(l1.finishT, l2.finishT);
        }
    });
    
    // 강의실 체크
    for(Lecture lec : lectures) {
    	boolean vacume = false; //빈 강의실 있는가
    	
    	for(int i = 0;i<cnt;i++) {
    		if (nowend[i]<=lec.startT) {
    			nowend[i] = lec.finishT;
    			vacume = true; //ㅇㅇ 있으니깐 cnt++ 안해도 됨
    			break;
    		}
    	}
    	
    	if (!vacume) { // 빈 강의실 없어. 지금 수업할 곳 필요해. cnt++
    		nowend[cnt++] = lec.finishT;
    	}
    	
    }

    System.out.println(cnt);
	}

}
