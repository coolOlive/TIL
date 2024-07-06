import java.util.Scanner;
import java.io.FileInputStream;
 
// 논리제어/1대1 가위바위보/D1

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
        String game = sc.nextLine();
        String[] aWin = {"3 2","2 1","1 3"};
        String ans = "B";
        sc.close();
         
        for (int i = 0; i < 3; i++) {
            if (game.equals(aWin[i])) {
                ans = "A";
                break;
            }
        }
        System.out.println(ans);
    }
}