import java.io.*;
import java.util.*;

// 구현/배열 돌리기 3/골드5

public class JUN16935_RotatingArray3_박유진 {
	static int n,m,r,mid;
	static int[][] board,bo1,bo2,bo3,bo4;
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		board = new int[n][m];
		
		for(int i=0;i<n;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<m;j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<r;i++) {
			rotate(Integer.parseInt(st.nextToken()));
		}
		
		for(int[] b : board) {
			for(int a:b) {
				System.out.print(a+" ");
			}
			System.out.println();
		}
	}
	
	// 연산자에 따라 함수 실행
	static void rotate(int oper) {
		switch (oper) {
		case 1:
			op1();
			break;
		case 2:
			op2();
			break;
		case 3:
			op3();
			break;
		case 4:
			op4();
			break;
		case 5:
			op5();
			break;
		default:
			op6();
		}
	}
	
	// 상하반전
	static void op1() {
		for (int i=0;i<board.length/2;i++) {
			int[] tmp = board[i];
			board[i] = board[n-i-1];
			board[n-i-1] = tmp;
		}
	}
	
	// 좌우반전
	static void op2() {
	    for(int i=0;i<n; i++) {
	        for(int j=0;j<m/2;j++) {
	            int tmp = board[i][j];
	            board[i][j] = board[i][m-j-1];
	            board[i][m-j-1] = tmp;
	        }
	    }
	}
	
	// 오른쪽으로 90도 회전
	static void op3() {
	    int[][] tmp = new int[m][n];
	    
	    for(int i = 0; i < m; i++) {
	        for(int j = 0; j < n; j++) {
	            tmp[i][n-1-j] = board[j][i];
	        }
	    }
	    
	    board = tmp;
	    int temp = n;
	    n = m;
	    m = temp;
	}

	// 왼쪽으로 90도 회전
	static void op4() {
	    int[][] tmp = new int[m][n];
	    
	    for(int i = 0; i < m; i++) {
	        for(int j = 0; j < n; j++) {
	            tmp[m-1-i][j] = board[j][i];
	        }
	    }
	    
	    board = tmp;
	    int temp = n;
	    n = m;
	    m = temp;
	}
	
	// board 4조각으로 나누기
	static void divBoard() {
		bo1 = new int[n/2][m/2];
		bo2 = new int[n/2][m/2];
		bo3 = new int[n/2][m/2];
		bo4 = new int[n/2][m/2];
		
		for(int i=0;i<n/2;i++) {
			for(int j=0;j<m/2;j++) {
				bo1[i][j] = board[i][j];
				bo2[i][j] = board[i][m/2+j];
				bo3[i][j] = board[n/2+i][m/2+j];
				bo4[i][j] = board[n/2+i][j];
			}
		}
	}
	
	// 시계방향 회전 (4분할 1-2-3-4-1)
	static void op5() {
		divBoard();
		for(int i=0;i<n/2;i++) {
			for(int j=0;j<m/2;j++) {
				board[i][j] = bo4[i][j];
				board[i][m/2+j] = bo1[i][j];
				board[n/2+i][m/2+j] = bo2[i][j];
				board[n/2+i][j] = bo3[i][j];
			}
		}
	}
	
	// 반시계방향 회전 (4분할 4-3-2-1-4)
	static void op6() {
		divBoard();
		for(int i=0;i<n/2;i++) {
			for(int j=0;j<m/2;j++) {
				board[i][j] = bo2[i][j];
				board[i][m/2+j] = bo3[i][j];
				board[n/2+i][m/2+j] = bo4[i][j];
				board[n/2+i][j] = bo1[i][j];
			}
		}
	}
}
