struct Solution;

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let m = matrix.len();
        let n = matrix[0].len();
        let (mut i, mut j) = (0, m * n - 1);
        while i < j {
            let m = i + (j - i) / 2;
            let value = matrix[m/n][m%n];
            if value == target {
                return true;
            } else if value < target {
                i = m + 1;
            } else {
                j = m;
            }
        }
        matrix[i/n][i%n] == target
    }
}