// Q-link: https://www.codechef.com/problems/BUDGET25

import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef {
    public static void main(String[] args) throws java.lang.Exception {
        // your code goes here
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int x = sc.nextInt();
            ArrayList<Integer> arr = new ArrayList();
            long count = 0;
            long surplus = 0;
            while (n-- > 0) {
                int a = sc.nextInt();
                if (a >= x) {
                    count++;
                    surplus += a - x;
                } else {
                    arr.add(x - a);
                }
            }
            Collections.sort(arr);
            for (int el : arr) {
                if (surplus >= el) {
                    count++;
                    surplus -= el;
                } else
                    break;
            }
            System.out.println(count);
        }

    }
}
