import java.util.Scanner;
import java.io.FileInputStream;

// 구현/숫자 정사각형/실버3

public class s3_1051 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		String tmp;
		String[][] board = new String[n][m];
		int ans = 1;
		int under = Math.min(n, m);
		
		for(int i = 0;i<n;i++) {
			tmp = sc.next();
			for (int j = 0;j<m;j++) {
				board[i][j] = String.valueOf(tmp.charAt(j));
			}
		}
		
		for (int i = 0;i<n;i++) {
			for (int j = 0;j<m;j++) {
				String aa = board[i][j];
				for (int k = 1; k < under;k++) {
					if (i+k<n && j+k<m) {
						if (aa.equals(board[i + k][j]) &&
							aa.equals(board[i][j + k]) &&
							aa.equals(board[i + k][j + k])) {
	                            ans = Math.max(ans, (k + 1) * (k + 1));
	          }
					}
					
				}
			}
		}
		System.out.println(ans);

	}

}


