import java.util.*;
import java.io.*;

public class Main {
		public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer stk = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(stk.nextToken());
		int K = Integer.parseInt(stk.nextToken());
		
		int[] W = new int[N+1];
		int[] V = new int[N+1];
		
		for(int i = 1; i < N + 1; i++) {
			StringTokenizer stk2 = new StringTokenizer(br.readLine());
			W[i] = Integer.parseInt(stk2.nextToken());
			V[i] = Integer.parseInt(stk2.nextToken());
		}
		
		int res = 0;
		// dp[i번째 아이템][무게] = i번째 아이템이 해당 무게에서 가지는 가치
		int[][] dp = new int[N+1][K+1];
		
		for(int i = 1; i < N+1; i++) { // i번째 아이템
			for(int j = 1; j < K+1; j++) { // i번째 아이템의 무게
				// 기본적으로 이전 아이템의 가치를 저장
				dp[i][j] = dp[i-1][j];
				// 가능한 값과 비교
				if(j - W[i] >= 0) { // 현재 무게에서 내 무게를 제외했을때, 남는 무게가 존재한다면
					// 이전 값을 그대로 할 것인지, 이전 아이템의 남은 무게에 해당하는 가치+현재아이템의 가치 중 큰 것을 선택
					dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-W[i]]+V[i]);
				}
			}
		}
		
		
		System.out.println(dp[N][K]);
		
	}
		
	}
