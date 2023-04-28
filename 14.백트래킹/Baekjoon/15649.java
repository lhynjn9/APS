import java.util.*;
import java.io.*;

public class 보석상자_이현정 {
	
	static int[] arr;
	static boolean[] visited;
	static int N, M;

	
	public static void main(String[] args) throws Exception{
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer stk = new StringTokenizer(br.readLine());
		N = Integer.parseInt(stk.nextToken());
		M = Integer.parseInt(stk.nextToken());
		
		visited = new boolean[N+1];
		arr = new int[N+1];
		
		perm(0);

	}
	
	public static void perm(int idx) {
		if(idx == M) {
			for (int i = 0; i < M; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
			return;
		}
		
		for(int i=1; i <= N; i++) {
			// 아직 방문하지 않은 수라면
			if(!visited[i]) {
				visited[i] = true;
				arr[idx] = i;
				perm(idx+1); // 다음 것 탐색
				visited[i] = false;
			}
		}
	}
}                                                                  