struct Solution;

use std::collections::VecDeque;

impl Solution {
    pub fn maximum_beauty(mut nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        if n < 2 { return n as i32; }
        nums.sort_unstable();
        let mut deq = VecDeque::from([nums[0]]);
        let mut beauty = 1;
        for i in 1..n {
            deq.push_back(nums[i]);
            while deq.len() > 0 && *deq.front().unwrap() < nums[i] - 2 * k {
                deq.pop_front();
            }
            beauty = beauty.max(deq.len());
        }
        beauty as i32
    }

    pub fn maximum_beauty_binary_search(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut beauty = 1;
        for (ni, num) in nums.iter().enumerate() {
            // look for nj that is the first that num + k < nums[nj] - k
            let (mut i, mut j) = (ni + 1, nums.len() - 1);
            if i > j { break; }
            while i < j {
                let m = i + (j - i) / 2;
                if num + k >= nums[m] - k {
                    i = m + 1;
                } else {
                    j = m;
                }
            }
            let nj = if num + k < nums[i] - k { i } else { i + 1 };
            beauty = beauty.max(nj - ni);
        }
        beauty as i32
    }
}

fn main() {
    println!("{}", Solution::maximum_beauty_binary_search(vec![4,6,1,2], 2));
    println!("{}", Solution::maximum_beauty(vec![1,1,1,1], 10));
    println!("{}", Solution::maximum_beauty(vec![52,34], 21));
}