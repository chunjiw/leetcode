struct Solution;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut result = vec![];
        let mut prev = i32::MAX;
        for i in (2..nums.len()).rev() {
            if nums[i] == prev {
                continue;
            }
            let pairs = Self::two_sum(&nums[0..i], -nums[i]);
            for mut pair in pairs {
                pair.push(nums[i]);
                result.push(pair);
            }
            prev = nums[i];
        }
        result
    }

    pub fn two_sum(sorted_nums: &[i32], target: i32) -> Vec<Vec<i32>> {
        let mut result = vec![];
        let (mut i, mut j) = (0, sorted_nums.len() - 1);
        while i < j {
            let s = sorted_nums[i] + sorted_nums[j];
            if s == target {
                result.push(vec![sorted_nums[i], sorted_nums[j]]);
                i += 1;
            } else if s < target {
                i += 1;
            } else {
                j -= 1;
            }
        }
        result.dedup();    // result is sorted, so dedup() remove all duplicates.
        result
    }
}

fn main() {
    Solution::three_sum(vec![-1,0,1,2,-1,-4]);
}
