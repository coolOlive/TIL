package com.baekjoon2;

// 다음순열/순열/실버3

import java.io.*;
import java.util.*;

public class Main_9742 {
    static char[] arr;
    static int cnt;
    static int current;
    static boolean found;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while ((line = br.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
            String inputStr = st.nextToken();
            cnt = Integer.parseInt(st.nextToken());
            arr = inputStr.toCharArray();
            current = 0;
            found = false;
            
            do {
                current++;
                if (current == cnt) {
                    System.out.println(inputStr + " " + cnt + " = " + String.valueOf(arr));
                    found = true;
                    break;
                }
            } while (np(arr));

            if (!found) {
                System.out.println(inputStr + " " + cnt + " = No permutation");
            }
        }
    }

    // 다음 순열을 찾는 함수
    static boolean np(char[] p) {
        int n = p.length;
        int i = n - 1;

        // 꼭대기 찾기
        while (i > 0 && p[i - 1] >= p[i]) --i;
        if (i == 0) return false; // 다음 순열이 없음

        // 교환할 자리 찾기
        int j = n - 1;
        while (p[i - 1] >= p[j]) --j;

        // 자리바꾸기
        swap(p, i - 1, j);

        // 정점 뒤에꺼 정렬
        int k = n - 1;
        while (i < k) swap(p, i++, k--);

        return true;
    }

    // 자리 바꿈
    static void swap(char[] p, int i, int j) {
        char tmp = p[i];
        p[i] = p[j];
        p[j] = tmp;
    }
}
