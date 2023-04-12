import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[1000001];
		
		dp[0] = 0;
		dp[1] = 0;
		
		for (int i = 2; i <= n; i++) {
			dp[i] = dp[i - 1] + 1; // 먼저 1을 빼준다 
            if (i % 2 == 0) dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            if (i % 3 == 0) dp[i] = Math.min(dp[i], dp[i / 3] + 1);
			
		}
		
		System.out.println(dp[n]);
	}
	
}                                                                   