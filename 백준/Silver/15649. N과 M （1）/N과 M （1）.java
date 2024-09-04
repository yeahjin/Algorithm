import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] v = new boolean[n];
		int[] sel = new int[m];
		recursive(n,m,v,sel,0);
	}

	private static void recursive(int n, int m, boolean[] v, int[] sel, int idx) {
		if(idx == m) {
			for (int val : sel) {
				System.out.print(val + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = 0; i < n; i++) {
			if(v[i] == false) {
				v[i] = true;
				sel[idx] = i +1;
				recursive(n, m, v, sel, idx+1);
				v[i] = false;
			}
		}
	}

}
