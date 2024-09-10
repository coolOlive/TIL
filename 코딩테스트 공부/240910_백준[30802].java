package com.baekjoon2;

// 수학,구현/웰컴 키트/브론즈3

import java.util.Scanner;

public class Main_30802 {
	static int[] ts = new int[6];
	static int t,p,anst=0,ansp=0,people;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		people = sc.nextInt();
		
		for(int i=0;i<6;i++) {
			ts[i] = sc.nextInt();
		}
		t = sc.nextInt();
		p = sc.nextInt();

		for(int i=0;i<6;i++) {
			if(ts[i]%t>0) {
				anst += ts[i]/t+1;
			} else {
				anst += ts[i]/t;
			}
		}
		
		System.out.println(anst);
		System.out.println(people/p+" "+people%p);
	}

}
