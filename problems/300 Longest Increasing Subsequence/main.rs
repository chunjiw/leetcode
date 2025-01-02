impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![1; nums.len()];
        let mut result = 1;
        for (i, num) in nums.iter().enumerate() {
            for j in 0..i {
                if nums[j] < *num {
                    dp[i] = dp[i].max(dp[j] + 1);
                    result = result.max(dp[i]);
                }
            }
        }
        result
    }
}
