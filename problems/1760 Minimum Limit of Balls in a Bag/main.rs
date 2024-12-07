struct Solution;

impl Solution {
    pub fn minimum_size_time_limit_exceeded(nums: Vec<i32>, max_operations: i32) -> i32 {
        let s: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut max_in_bag = (s / (nums.len() as i64 + max_operations as i64)) as i32;
        max_in_bag = max_in_bag.max(1);
        loop {
            let mut ops_left = max_operations;
            for num in &nums {
                let mut ops = num / max_in_bag;
                if num % max_in_bag == 0 {
                    ops -= 1;
                }
                ops_left -= ops;
                if ops_left < 0 {
                    break;
                }
            }
            if ops_left < 0 {
                max_in_bag += 1;
            } else {
                return max_in_bag;
            }
        }
    }
}

fn main() {
    println!("{}", Solution::minimum_size_time_limit_exceeded(vec![9], 2));
    println!("{}", Solution::minimum_size_time_limit_exceeded(vec![2,4,8,2], 4));
    println!("{}", Solution::minimum_size_time_limit_exceeded(vec![1,4,8,3], 4));
}