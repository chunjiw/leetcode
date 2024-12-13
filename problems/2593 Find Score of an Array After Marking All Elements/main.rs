struct Solution;

impl Solution {
    pub fn find_score(mut nums: Vec<i32>) -> i64 {
        let mut score = 0;
        loop {
            if let Some((index, value)) = nums.iter().enumerate().min_by_key(|&(_, value)| value) {
                if *value == i32::MAX { return score; }
                score += *value as i64;
                nums[index] = i32::MAX;
                if index >= 1 { nums[index-1] = i32::MAX; }
                if index + 1 < nums.len() { nums[index+1] = i32::MAX; }
            } else {
                return score;
            }
        }
    }
}

fn main() {
    println!("{}", Solution::find_score(vec![2,1,3,4,5,2]));
}