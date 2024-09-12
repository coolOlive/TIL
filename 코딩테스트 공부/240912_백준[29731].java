package com.baekjoon2;

import java.util.Scanner;

// 구현,문자열/2033년 밈 투표/브론즈5
// 마라톤 문제

public class Main_29731 {
    static int n;
    static boolean hack = false;
    static String[] promiss = {
            "Never gonna give you up",
            "Never gonna let you down",
            "Never gonna run around and desert you",
            "Never gonna make you cry",
            "Never gonna say goodbye",
            "Never gonna tell a lie and hurt you",
            "Never gonna stop"
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            String tmp = sc.nextLine();
            boolean isValid = false;

            for (int j = 0; j < promiss.length; j++) {
                if (promiss[j].equals(tmp)) {
                    isValid = true;
                    break;
                }
            }

            if (!isValid) {
                hack = true;
                break;
            }
        }

        System.out.println(hack ? "Yes" : "No");
    }
}
