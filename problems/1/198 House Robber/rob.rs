struct Solution;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        } else if n == 1 {
            return nums[0];
        }
        let mut sol = vec![nums[0]; n];
        sol[0] = nums[0];
        sol[1] = nums[0].max(nums[1]);
        for i in 2..n {
            sol[i] = sol[i-1].max(sol[i-2] + nums[i]);
        }
        sol[n-1]
    }
}

fn main() {
    println!("{}", Solution::rob(vec![]));
}