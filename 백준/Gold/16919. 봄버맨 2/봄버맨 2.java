import java.util.*;

public class Main {
	static int[] dr = { 0, 0, 1, -1 };
	static int[] dc = { 1, -1, 0, 0 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt(); // 세로
		int c = sc.nextInt(); // 가로
		int n = sc.nextInt(); // n초 후

		String arr[][] = new String[r][c];
		String arr2[][] = new String[r][c];
		String arr3[][] = new String[r][c];
		String arr4[][] = new String[r][c];

		for (int i = 0; i < r; i++) {
			String tmp = sc.next();
			for (int j = 0; j < c; j++) {
				String value = String.valueOf(tmp.charAt(j));
				arr[i][j] = value;
				arr2[i][j] = "O";
				arr3[i][j] = "O";
				arr4[i][j] = "O";

			}
		}
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				String value = arr[i][j];
				if (value.equals("O")) {
					arr3[i][j] = ".";
					for (int k = 0; k < 4; k++) {
						int cr = dr[k] + i;
						int cc = dc[k] + j;
						if (cr >= 0 && cr < r && cc >= 0 && cc < c) {
							arr3[cr][cc] = ".";
						}
					}

				}

			}
		}
//		System.arraycopy(arr3, 0, arr4, 0, arr4.length);
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				String value = arr3[i][j];
				if (value.equals("O")) {
					arr4[i][j] = ".";
					for (int k = 0; k < 4; k++) {
						int cr = dr[k] + i;
						int cc = dc[k] + j;
						if (cr >= 0 && cr < r && cc >= 0 && cc < c) {
							arr4[cr][cc] = ".";
						}
					}

				}

			}
		}

		if(n == 1) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					System.out.print(arr[i][j]);
				}
				System.out.println();
			}
		}
		else if (n % 2 == 0) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					System.out.print(arr2[i][j]);
				}
				System.out.println();
			}
		}
		else if (n>1 && n%4==1) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					System.out.print(arr4[i][j]);
				}
				System.out.println();
			}
		}
		else if(n > 1 && n % 4 == 3) {
			for (int i = 0; i < r; i++) {
				for (int j = 0; j < c; j++) {
					System.out.print(arr3[i][j]);
				}
				System.out.println();
			}
		}
	}

}
