import java.util.*;

public class Main {
	static int n;
	static int k;
	static int[] visited = new int[100001];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		int result = bfs(n);
		System.out.println(result);

	}

	private static int bfs(int node) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(node);
		visited[node] = 1;
		while (!q.isEmpty()) {
			int n = q.poll();
			if (n == k) {
				return visited[n] - 1;
			} if (n - 1 >= 0 && visited[n - 1] == 0) {
				visited[n - 1] = visited[n] + 1;
				q.add(n - 1);
			} if (n + 1 <= 100000 && visited[n + 1] == 0) {
				visited[n + 1] = visited[n] + 1;
				q.add(n + 1);
			} if (n * 2 <= 100000 && visited[n * 2] == 0) {
				visited[n * 2] = visited[n] + 1;
				q.add(n * 2);
			}
		}
		return -1;
	}

}
