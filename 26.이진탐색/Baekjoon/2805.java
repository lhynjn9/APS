import java.util.*;
import java.io.*;

public class 나무자르기_이현정 {
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer stk;
		stk = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(stk.nextToken());
		int M = Integer.parseInt(stk.nextToken());
		
		StringTokenizer stk1;
		stk1 = new StringTokenizer(br.readLine());
		
		int[] arr = new int[N];
		
		for (int i=0; i < N; i++) {
			arr[i] = Integer.parseInt(stk1.nextToken());
		}
		
		Arrays.sort(arr);
		
		int ans = check(arr, M);
		
		System.out.println(ans);
	}
	
	public static int check(int[] arr, int M) {
		int N = arr.length;
		int start = 0;
		int end = arr[N - 1];
		int mid = (start + end) / 2;
		
		while(start <= end) {
			mid = (start + end) / 2;
			long res = 0;
			
			for(int i= 0; i < N; i++) {
				if(arr[i] > mid) {
					res += (arr[i] - mid);
				}
			}
			
			// 얻으려는 길이보다 합이 작다면, 자르려는 높이를 낮춰서
			// 더 많은 나무가 잘리게 해야함
			if(res < M) {
				end = mid - 1;
			}
			
			// 얻으려는 길이보다 합이 크거나 같다면, 자르려는 높이를 높여
			// 최대 나무 길이을 구해야함
			else if(res >= M) {
				start = mid + 1; 
			}
		}
		return end;
	}
}                                                                   