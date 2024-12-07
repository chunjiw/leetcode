struct Solution;

impl Solution {

    pub fn minimum_size(nums: Vec<i32>, max_operations: i32) -> i32 {
        let s: i64 = nums.iter().map(|&x| x as i64).sum();
        let mut low = (s / (nums.len() as i64 + max_operations as i64)) as i32;
        low = low.max(1);
        let mut high = nums.iter().max().unwrap().clone();
        if Self::enough(&nums, max_operations, low) {
            return low;
        }
        while low + 1 < high {
            // Here gaurantee low is not enough, and high is enough
            let mid = (low + high) / 2;
            if Self::enough(&nums, max_operations, mid) {
                high = mid
            } else {
                low = mid
            }
        }
        high
    }

    pub fn enough(nums: &Vec<i32>, max_operations: i32, max_in_bag: i32) -> bool {
        let mut ops_left = max_operations;
        for num in nums {
            let mut ops = num / max_in_bag;
            if num % max_in_bag == 0 {
                ops -= 1;
            }
            ops_left -= ops;
            if ops_left < 0 {
                return false;
            }
        }
        true
    }

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
    println!("{}", Solution::minimum_size(vec![9], 2));
    println!("{}", Solution::minimum_size(vec![2,4,8,2], 4));
    println!("{}", Solution::minimum_size(vec![1,4,8,3], 4));
}