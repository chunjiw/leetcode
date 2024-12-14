impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let mark = matrix.iter().flatten().sum::<i32>() + 1;
        for i in 0..matrix.len() {
            for j in 0..matrix[0].len() {
                if matrix[i][j] != 0 { continue; }
                for k in 0..matrix.len() {
                    matrix[k][j] = if matrix[k][j] != 0 { mark } else { 0 };
                }
                for k in 0..matrix[0].len() {
                    matrix[i][k] = if matrix[i][k] != 0 { mark } else { 0 };
                }
            }
        }
        for i in 0..matrix.len() {
            for j in 0..matrix[0].len() {
                if matrix[i][j] == mark {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}