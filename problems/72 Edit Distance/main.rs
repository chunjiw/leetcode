struct Solution;

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let (m, n) = (word1.len(), word2.len());
        let mut dp: Vec<usize> = (0..n+1).collect();
        let mut ndp = dp.clone();
        for i in 1..m+1 {
            for j in 0..n+1 {
                if j == 0 {
                    ndp[j] = i;
                } else {
                    ndp[j] = (ndp[j-1] + 1).min(dp[j] + 1).min(
                        if word1.as_bytes().get(i-1) == word2.as_bytes().get(j-1) {
                            dp[j-1]
                        } else {
                            dp[j-1] + 1
                        }
                    )
                }
            }
            (dp, ndp) = (ndp, dp);
        }
        dp[n] as i32
    }
}