import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		ArrayList<int[]> arr = new ArrayList<int[]>();
		for (int i = 0; i < n; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			arr.add(new int[] { a, b });
		}
//		for (int i = 0; i < arr.size(); i++) {
//			System.out.print(arr.get(i)[0] + " " + arr.get(i)[1] + "\n");
//		}
		Collections.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
		Collections.sort(arr, (a, b) -> Integer.compare(a[1], b[1]));
		int cnt = 1;
		int start = arr.get(0)[0];
		int end = arr.get(0)[1];
		for (int i = 1; i < n; i++) {
			int nstart = arr.get(i)[0];
			int nend = arr.get(i)[1];
			if(end <= nstart) {
				start = nstart;
				end = nend;
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}
