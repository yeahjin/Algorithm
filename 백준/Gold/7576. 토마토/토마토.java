import java.util.*;

public class Main {
	static int[][] map;
	static int[][] date;
	static int m; // 가로
	static int n; // 세로
	static int cnt;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static Queue<Node> Q = new LinkedList<Node>();
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		m = sc.nextInt();
		n = sc.nextInt();
		map = new int[n][m];
		date = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				map[i][j] = sc.nextInt();
				if(map[i][j] == 1) {
					Q.offer(new Node(i, j));
				}

			}
		}
		bfs();
		int result = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if(map[i][j] == 0) {
					System.out.println(-1);
					return;
				}
				else {
					result = Math.max(result, date[i][j]);
				}
			}
		}
		System.out.println(result);
	}

	private static void bfs() {
		while(!Q.isEmpty()) {
			Node toma = Q.poll();
			for (int i = 0; i < 4; i++) {
				int nx = toma.x + dx[i];
				int ny = toma.y + dy[i];
				if(nx >= 0 && nx < n && ny >= 0 && ny < m&&map[nx][ny] == 0) {
					map[nx][ny] = 1;
					Q.offer(new Node(nx,ny));
					date[nx][ny] = date[toma.x][toma.y] + 1;
				}
			}
		}
	}

	private static void print(int[][] map) {
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[i].length; j++) {
				System.out.print(map[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}
	
	static class Node{
		int x;
		int y;
		Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}
