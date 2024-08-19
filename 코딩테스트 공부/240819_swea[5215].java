package com.swea;

import java.util.*;

// nextpermutation,부분집합/햄버거 다이어트/D3

public class SW5215_HamburgerDietNP_박유진 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();  // 테케 수

        for (int tc = 1; tc <= T; tc++) {
            int N = sc.nextInt();  // 재료 수
            int L = sc.nextInt();  // 최대 칼로리

            int[] t = new int[N];
            int[] c = new int[N];

            for (int i = 0; i < N; i++) {
                t[i] = sc.nextInt();
                c[i] = sc.nextInt();
            }

            int maxT = 0;

            // 각 부분집합의 크기 결정
            for (int r=1;r<=N;r++) {
                int[] minsBuger = new int[N];
                for (int i = N-r; i < N; i++) {
                    minsBuger[i] = 1;
                }

                do {
                    int sumT = 0;
                    int sumC = 0;

                    for (int i = 0; i < N; i++) {
                        if (minsBuger[i] == 1) {
                            sumT += t[i];
                            sumC += c[i];
                        }
                    }

                    if (sumC <= L) {  //칼로리 제한 안 넘을 떄
                        maxT = Math.max(maxT,sumT);
                    }

                } while (np(minsBuger));
            }

            System.out.println("#"+tc+" "+maxT);
        }
        sc.close();
    }

    static boolean np(int[] p) {  // 다음 순열 생성
        int N = p.length;
        if (N <= 1) return false; // 배열의 크기가 1 이하일 경우 순열이 없음

        // step1) 꼭대기 찾기
        int i = N - 1;
        while (i > 0 && p[i-1] >= p[i]) --i;

        if (i == 0) return false;  // 다음 순열이 없음

        // tep2) 꼭대기 앞 교환 위치에 교환할 값이 들어있는 자리 찾기
        int j = N - 1;
        while (p[i-1] >= p[j]) --j;

        // step3) 두 위치의 수 교환
        swap(p,i-1, j);

        // step4) 꼭대기부터 맨 뒤까지 오름차순으로 정렬
        int k = N-1;
        while (i < k) {
            swap(p, i++, k--);
        }

        return true;  //다음 순열 존재
    }

    static void swap(int[] p, int i, int j) {
        int temp = p[i];
        p[i]=p[j];
        p[j]=temp;
    }
}
