struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len(); // `n` is a runtime-determined value
        let mut incum = vec![1; n]; // Dynamic vector to track prefix products
        let mut decum = vec![1; n]; // Dynamic vector to track suffix products
        for i in 1..n {
            incum[i] = incum[i-1] * nums[i-1];
        }
        for i in (0..n-1).rev() {
            decum[i] = decum[i+1] * nums[i+1];
            incum[i] *= decum[i]
        }
        incum
    }
}

fn main() {
    println!("{:?}", Solution::product_except_self(vec![]));
}