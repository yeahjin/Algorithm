import java.util.*;
public class Main {
	static boolean[] visited;
	static String[] arr;
	static int l;
	static ArrayList<String> arr2 = new ArrayList<String>();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		l = sc.nextInt();
		int c = sc.nextInt();
		visited = new boolean[c];
		arr = new String[c];
		for (int i = 0; i < c; i++) {
			arr[i] = sc.next();
		}
		Arrays.sort(arr);
		
		combination(0,l);
		for (int i = arr2.size()-1; i >=0; i--) {
			System.out.println(arr2.get(i));
		}
	}
	private static void combination(int start, int r) {
		if(r==arr.length) {
			String tmp = new String();
			int cnt = 0;
			for (int i = 0; i < arr.length; i++) {
				if(!visited[i]) {
					if(arr[i].equals("a")||arr[i].equals("e")||arr[i].equals("i")||arr[i].equals("o")||arr[i].equals("u")) {
						cnt++;
					}
					tmp += arr[i];
					
				}
			}
			if(cnt >= 1 && l - cnt >= 2) {
				arr2.add(tmp);
			}
			return;
		}
		for (int i = start; i < arr.length; i++) {
			visited[i] = true;
			combination(i+1, r+1);
			visited[i] = false;
		}
	}

}
