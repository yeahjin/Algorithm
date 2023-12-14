import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static char[][] arr;
	static char[][] arr2;
	static boolean[][] visited;
	static int[] dx = { 0, 0, 1, -1 };
	static int n;
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		arr = new char[n][n];
		arr2 = new char[n][n];
		for (int i = 0; i < n; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < n; j++) {
				arr[i][j] = tmp.charAt(j);
				arr2[i][j] = tmp.charAt(j);
				if(arr[i][j] == 'G') {
					arr2[i][j] = 'R';
				}
			}
		}
		visited = new boolean[n][n];
		// 색약 아닌 사람
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (!visited[i][j]) {
					if (arr[i][j] == 'R') {
						bfs(i, j, 'R');
						cnt++;
					}
					else if(arr[i][j] == 'B') {
						bfs(i,j,'B');
						cnt++;
					}
					else {
						bfs(i,j,'G');
						cnt++;
					}
				}
			}
		}
		// 색약인 사람
		int cnt2 = 0;
		arr = arr2;
		visited = new boolean[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (!visited[i][j]) {
					if (arr[i][j] == 'R') {
						bfs(i, j, 'R');
						cnt2++;
					}
					else if(arr[i][j] == 'B') {
						bfs(i,j,'B');
						cnt2++;
					}
				}
			}
		}
		System.out.println(cnt + " " + cnt2);

	}

	private static void bfs(int i, int j, char s) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] { i, j });
		visited[i][j] = true;
		while (!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
			for (int k = 0; k < 4; k++) {
				int cx = x + dx[k];
				int cy = y + dy[k];
				if (cx >= n || cy >= n || cx < 0 || cy < 0 || arr[cx][cy] != s || visited[cx][cy])
					continue;
				q.add(new int[] { cx, cy });
				visited[cx][cy] = true;

			}

		}
	}

}
