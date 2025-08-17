struct Solution;

impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result = vec![];
        let (m, n) = (matrix.len(), matrix[0].len());
        let p = m.min(n) / 2;
        let odd = m.min(n) % 2 == 1;
        for i in 0..p {
            result.extend_from_slice(&matrix[i][i..n-i]);
            for r in i+1..m-i-1 {
                result.push(matrix[r][n-i-1]);
            }
            for c in (i+1..n-i).rev() {
                result.push(matrix[m-i-1][c]);
            }
            for r in (i+1..m-i).rev() {
                result.push(matrix[r][i]);
            }
        }
        if odd {
            if n >= m {
                result.extend_from_slice(&matrix[m/2][m/2..n-m/2]);
            } else {
                for r in n/2..m-n/2 {
                    result.push(matrix[r][n/2]);
                }
            }
        }
        result
    }
}