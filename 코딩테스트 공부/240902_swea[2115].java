import java.io.*;
import java.util.*;

// 순조부/벌꿀채취/[모의 SW 역량테스트]

public class Solution {
	static int n, m, c;
	static int[][] honey;
	static int maxProfit;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {

			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			honey = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					honey[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			maxProfit = 0;

			// 두 일꾼이 다른 행에서 선택해야함.
			for (int i = 0; i < n; i++) {
				for (int j = 0; j <= n - m; j++) {

					int work1 = honeyMax(i, j);

					// 같은 행에서 다른통
					for (int k = j + m; k <= n - m; k++) {
						int work2 = honeyMax(i, k);
						maxProfit = Math.max(maxProfit, work1 + work2);
					}

					// 다른행에서 통 선택
					for (int i2 = i + 1; i2 < n; i2++) {
						for (int k = 0; k <= n - m; k++) {
							int work2 = honeyMax(i2, k);
							maxProfit = Math.max(maxProfit, work1 + work2);
						}
					}
				}
			}

			System.out.println("#" + tc + " " + maxProfit);
		}
	}

	// 연속된 통에서 꿀벌 이익
	static int honeyMax(int x, int y) {
		int[] tmp = new int[m]; // 벌꿀 양 저장 배열
		int sum = 0; // 지금 꿀통에이쓴ㄴ 꿀 총합
		int profit = 0; // 꿀통 이익*

		for (int i = 0; i < m; i++) {
			tmp[i] = honey[x][y + i];
			sum += tmp[i];
			profit += tmp[i] * tmp[i];
		}

		if (sum <= c) { // 꿀이 c개 이하
			return profit;
		}

		return profitCal(tmp, 0, 0, 0); // c개보다 많을 때
	}

	// totalhoney가 c 안넘게 최대 이익 계산하기_연속된m개의 통
	static int profitCal(int[] temp, int cnt, int sum, int profit) {
		if (sum > c) {
			return 0;
		}

		if (cnt == m) {
			return profit;
		}

		int yes = profitCal(temp, cnt + 1, sum + temp[cnt], profit + temp[cnt] * temp[cnt]);
		int no = profitCal(temp, cnt + 1, sum, profit);

		return Math.max(yes, no);
	}
}
