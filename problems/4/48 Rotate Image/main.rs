struct Solution;

impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();
        let m = n / 2;    // m layers need to rotate
        let mut hold = 0;
        for k in (0..m) {
            // for 0th layer, l is in 0..n-1
            // for 1th layer, l is in 1..n-1-1
            let g = n - k - 1;
            // for k+l in k..g
            for l in 0..g-k {
                hold = matrix[k][k+l];
                matrix[k][k+l] = matrix[g-l][k];
                matrix[g-l][k] = matrix[g][g-l];
                matrix[g][g-l] = matrix[k+l][g];
                matrix[k+l][g] = hold;
            }
        }
    }
}

