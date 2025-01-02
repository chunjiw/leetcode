impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let mut dp = vec![-1; amount as usize + 1];
        dp[0] = 0;
        for i in 1..dp.len() {
            let mut mincount = i32::MAX;
            for coin in &coins {
                let delta = *coin as usize;
                if i >= delta && dp[i-delta] != -1 {
                    mincount = mincount.min(dp[i-delta] + 1);
                    dp[i] = mincount
                }
            }
        }
        dp[amount as usize]
    }
}