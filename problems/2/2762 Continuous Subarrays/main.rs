struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn continuous_subarrays(nums: Vec<i32>) -> i64 {
        let (mut i, mut j) = (0, 0);
        let mut result: i64 = 0;
        let mut map = HashMap::new();
        while j < nums.len() {
            *map.entry(nums[j]).or_insert(0) += 1;
            j += 1;
            while *map.keys().max().unwrap() - *map.keys().min().unwrap() > 2 {
                let count = map.get_mut(&nums[i]).unwrap();
                *count -= 1;
                if *count <= 0 {
                    map.remove(&nums[i]);
                }
                i += 1;
            }
            result += (j - i) as i64;
        }
        result
    }
}

fn main() {
    println!("{}", Solution::continuous_subarrays(vec![5,4,2,4]));
}