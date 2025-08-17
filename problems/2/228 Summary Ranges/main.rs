struct Solution;

impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut result = vec![];
        if nums.is_empty() {
            return result;
        }
        
        let mut from = nums[0];

        for (i, num) in nums.iter().enumerate() {
            if i + 1 == nums.len() || num + 1 < nums[i+1] {
                if from == *num {
                    result.push(from.to_string());
                } else {
                    result.push(format!("{}->{}", from, num));
                }
                if i + 1 < nums.len() {
                    from = nums[i + 1];
                }
            }
        }
        result
    }
}

fn main() {
    println!("{:?}", Solution::summary_ranges(vec![0,1,2,4,5,7]));
}