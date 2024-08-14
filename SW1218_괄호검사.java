package sweaSolving;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class SW1218_PairingParenthesis_박유진 {
	static int n, ans;
    static String[] open = {"(","[","{","<"};
    static String[] close = {")","]","}",">"};

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 1; i <= 10; i++) {
        	ans = 0;
            n = Integer.parseInt(br.readLine()); // 괄호 문자열 길이
            String input = br.readLine(); // 괄호 문자열 입력

            if(check(input)) ans = 1;

            System.out.printf("#%d %d\n", i, ans);
        }
    }

    private static boolean check(String input) {
        Stack<Character> stack = new Stack<>();

        for (int j = 0; j < n; j++) {
            char c = input.charAt(j);

            if (isOpenBracket(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty() || !isPair(stack.pop(),c)){
                    return false;
                }
            }
        }

        return stack.isEmpty(); // 모든 여는 괄호가 짝을 찾았는지 확인
    }

    private static boolean isOpenBracket(char c) {
        for (String o : open) {
            if (c == o.charAt(0)) {
                return true;
            }
        }
        return false;
    }

    private static boolean isPair(char oo, char cc) {
        for (int i = 0; i < open.length; i++) {
            if (oo == open[i].charAt(0) && cc == close[i].charAt(0)) {
                return true;
            }
        }
        return false;
    }
}
