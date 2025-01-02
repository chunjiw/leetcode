impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {
        let mut dp = vec![];
        let mut ndp = vec![];
        for (i, row) in triangle.iter().enumerate() {
            if i == 0 {
                dp.push(row[0]);
                ndp.push(row[0]);
            } else {
                dp.push(0);
                ndp.push(0);
                for (j, num) in row.iter().enumerate() {
                    if j == 0 {
                        ndp[j] = dp[j] + num;
                    } else if j < row.len() - 1 {
                        ndp[j] = dp[j-1].min(dp[j]) + num;
                    } else {
                        ndp[j] = dp[j-1] + num;
                    }
                }
                (dp, ndp) = (ndp, dp);
            }
        }
        *dp.iter().min().unwrap()
    }
}
