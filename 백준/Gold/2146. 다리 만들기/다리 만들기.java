import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[][] map;
	static int n;
	static int ans = Integer.MAX_VALUE;
	static boolean visited[][];
	static ArrayList<int[]> groupSet;
	static int[] dx = { 0, 0, 1, -1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		map = new int[n][n];
		groupSet = new ArrayList<int[]>();
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// 1이면서 같은 그룹인지 확인하는 배열 만들기
		int group = 0;
		visited = new boolean[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (map[i][j] == 1 && !visited[i][j]) {
					groupCheckerMaker(i, j, group);
					group++;
				}
			}
		}
		
		for (int i = 0; i < groupSet.size(); i++) {
			int r = groupSet.get(i)[0];
			int c = groupSet.get(i)[1];
			int g = groupSet.get(i)[2];
			bfs(r,c, new boolean[n][n],g);
		}
		System.out.println(ans);
	}

	private static void bfs(int r, int c, boolean v[][],int g) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] {r,c,0});
		v[r][c] = true;
		while(!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
			int dis = now[2];
			for (int i = 0; i < 4; i++) {
				int cx = x + dx[i];
				int cy = y + dy[i];
				if (cx >= n || cy >= n || cx < 0 || cy < 0) continue;
				if (v[cx][cy]) continue;
				if(map[cx][cy] == 1) {
					if (groupChecker(cx,cy,g)) continue;
					ans = Integer.min(ans, dis);
					return;
				}
				q.add(new int[] {cx,cy,dis+1});
				v[cx][cy] = true;
			}
		}
	}
	// 같은 그룹인지 확인
	private static boolean groupChecker(int cx, int cy, int g) {
		for (int i = 0; i < groupSet.size(); i++) {
			if (groupSet.get(i)[0] == cx  && groupSet.get(i)[1] == cy) {
				if (groupSet.get(i)[2] == g) return true;
			}
		}
		return false;
	}

	private static void groupCheckerMaker(int r, int c, int group) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] {r,c});
		groupSet.add(new int[] {r,c,group});
		visited[r][c] = true;
		while(!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
			for (int i = 0; i < 4; i++) {
				int cx = x + dx[i];
				int cy = y + dy[i];
				if (cx >= n || cy >= n || cx < 0 || cy < 0) continue;
				if (visited[cx][cy] || map[cx][cy] == 0) continue;
				q.add(new int[] {cx,cy});
				visited[cx][cy] = true;
				groupSet.add(new int[] {cx,cy,group});
			}
		}
	}

	private static void print(int[][] map) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(map[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
	private static void print(boolean[][] map) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(map[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
}