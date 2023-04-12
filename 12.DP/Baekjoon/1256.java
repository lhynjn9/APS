import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int n = Integer.parseInt(br.readLine());
		int[] grape = new int[10001];
		
		for(int i=1; i < n+1; i++) {
			grape[i] = Integer.parseInt(br.readLine());
		}
		
		int[] score = new int[10001];
		
		score[1] = grape[1];
		score[2] = grape[1] + grape[2];
		score[3] = Math.max(score[2], Math.max(score[1] + grape[3], grape[2] + grape[3]));
		
		for(int i = 4; i < n+1; i++) {
			score[i] = Math.max(score[i - 1], Math.max(score[i - 2] + grape[i], score[i - 3] + grape[i - 1] + grape[i]));
		}
		
		System.out.println(score[n]);
	}
	
}                                                                   