impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut m = i64::MAX;
        let mut res: i64 = 0;
        let mut neg_singular: i64 = 0;
        for row in matrix {
            for num in row {
                let na = num.abs() as i64;
                res += na;
                if na < m {
                    m = na;
                }
                if num < 0 {
                    neg_singular = 1 - neg_singular;
                }
            }
        }
        res - neg_singular * 2 * m
    }
}