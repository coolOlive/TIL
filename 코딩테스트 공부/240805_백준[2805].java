package com.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 이분탐색/나무 자르기/s2

public class Main_2805 {
	static int n,m,maxTree;
	static long start,end,ans,mid,wood;
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        int[] trees = new int[n];
        st = new StringTokenizer(br.readLine());

        maxTree = 0;
        for (int i = 0; i < n; i++) {
            trees[i] = Integer.parseInt(st.nextToken());
            maxTree = Math.max(maxTree, trees[i]);
        }

        start = 0;
        end = maxTree;
        ans = 0;

        while (start <= end) {
            mid = (start + end) / 2;
            wood = 0;

            for (int tree: trees) {
                if (tree > mid) {
                    wood += (tree-mid);
                }
            }

            if (wood >= m) {
                start = mid+1;
                ans = mid;
                continue;
            }
            end = mid-1;
        }

        System.out.println(ans);
    }
}
