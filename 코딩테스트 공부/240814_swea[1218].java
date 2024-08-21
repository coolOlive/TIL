package sweaSolving;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

//_괄호검사

public class SW1218_PairingParenthesis_������ {
	static int n, ans;
    static String[] open = {"(","[","{","<"};
    static String[] close = {")","]","}",">"};

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 1; i <= 10; i++) {
        	ans = 0;
            n = Integer.parseInt(br.readLine()); // ��ȣ ���ڿ� ����
            String input = br.readLine(); // ��ȣ ���ڿ� �Է�

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

        return stack.isEmpty(); // ��� ���� ��ȣ�� ¦�� ã�Ҵ��� Ȯ��
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
