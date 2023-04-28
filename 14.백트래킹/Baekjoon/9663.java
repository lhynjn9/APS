import java.util.*;
import java.io.*;

public class Main {

	static int[] arr;
	static int N;
	static int de = 0;
	
	public static void main(String[] args) throws IOException {
		System.setIn(new FileInputStream("src/input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		
		dfs(0);
		System.out.println(de);
}
	// i는 열
	// depth는 행
	public static void dfs(int depth) {
		
		if(depth == N) {
			de++;
			return;
		}
		
		for(int i = 0 ; i < N; i++) {
			// depth행 i열에 값을 넣는다
			arr[depth] = i;
			// 해당 행 열에 값을 넣는 것이 가능한지 확인
			if(possible(depth)) {
				// 만약 가능하다면, 다음 행에 값을 넣을 수 있는지 확인한다
				dfs(depth+1);
			}
		}	
	}
	
	public static boolean possible(int row) { 
		// 행은 위에서 걸러지기 때문에 열과 대각선만 확인하면 됨
		for(int i = 0 ; i < row ; i++) {
		//행은 다르지만, 같은 열에 값이 있어서 불가
		if(arr[i]==arr[row]) {
			return false;
		}
		//대각선에 일치하는게 있는지 판별
		// 행의차와 열의차가 같으면 대각선에 놓여있는 경우  
		else if(Math.abs(row-i) == Math.abs(arr[row]-arr[i])) {
			return false;
		}
			
		}
		
		return true;
	}
}                                                            