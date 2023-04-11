import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			StringTokenizer stk = new StringTokenizer(br.readLine());
			
			int[] arr = new int[N];
			
			for(int j = 0; j < N; j++) {
				arr[j] = Integer.parseInt(stk.nextToken());
			}
			
			int res = 0;
			
			HashMap<Integer, Boolean> codes = new HashMap<Integer, Boolean>(N);
			
			for(int z = 0; z < N; z++) {
				codes.put(arr[z], true);
			}
			
			Arrays.sort(arr);
			
			for(int a = 0; a < N; a++) {
				for(int b = a+1; b < N; b++) {
					int c = arr[b]*2 - arr[a];
					if (codes.get(c) != null) {
						res += 1;
				}
			}
			}
			
			System.out.println(res);
			
		}
	}
}
