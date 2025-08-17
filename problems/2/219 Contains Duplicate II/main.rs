struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
        let mut map = HashMap::new();
        for (i, n) in nums.iter().enumerate() {
            let last_index = map.entry(n).or_insert(i);
            if *last_index == i { continue; }
            if i - *last_index <= k as usize { return true; }
            *last_index = i;
        }
        false
    }
}