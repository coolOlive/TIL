package com.baekjoon;

import java.util.Scanner;

// 백트래킹/좋은수열/골드4
//que로 풀었더니 메모리 초과! -> 재귀로 바꿈

public class Main_2661 {
    static int n;
    static String ans = "";
    static String[] nums = {"1","2","3"};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        backtrack("");
    }

    public static void backtrack(String now) {
        if (now.length() == n) {
            System.out.println(now);
            System.exit(0);
        }

        for (int i=0; i <3; i++) {
            if (check(now + nums[i])) {
                backtrack(now + nums[i]);
            }
        }
    }

    public static boolean check(String s) {
        int L = s.length();
        for (int j = 1; j <= L/2; j++) {
            String tmp1 = s.substring(L-j,L);
            String tmp2 = s.substring(L-(2*j),L-j);
            if (tmp1.equals(tmp2)) {
                return false;
            }
        }
        return true;
    }
}
