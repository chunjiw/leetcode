use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i, &num) in nums.iter().enumerate() {
            if let Some(&j) = map.get(&num) {
                // Found the solution, return indices
                return vec![j as i32, i as i32];
            } else {
                // Store the complement and its index
                map.insert(target - num, i);
            }
        }
        vec![] // Return an empty vector if no solution is found
    }
}

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let result = Solution::two_sum(nums, target);
    println!("{:?}", result); // Output: [0, 1]
}
