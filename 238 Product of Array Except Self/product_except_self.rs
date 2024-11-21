impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len(); // `n` is a runtime-determined value
        let mut incum = vec![1; n]; // Dynamic vector to track prefix products
        let mut decum = vec![1; n]; // Dynamic vector to track suffix products
        let mut result = vec![1; n];
        for i in 1..n {
            incum[i] = incum[i-1] * nums[i-1];
        }
        for i in (0..n-1).rev() {
            decum[i] = decum[i+1] * nums[i+1];
        }
        for i in 0..n {
            result[i] = incum[i] * decum[i];
        }
        result
    }
}