struct Solution;

impl Solution {

    pub fn find_score(nums: Vec<i32>) -> i64 {
        let mut score = 0;
        let mut sorted: Vec<(usize, i32)> = nums.iter().enumerate().map(|(i, &v)| (i, v)).collect();
        sorted.sort_by_key(|&(_, value)| value);
        let mut marked = vec![false; nums.len() + 1];
        for (i, value) in sorted {
            if marked[i] { continue; }
            score += value as i64;
            if i >= 1 { marked[i-1] = true; }
            marked[i+1] = true;
        }
        score
    }

    pub fn find_score_time_complexity_on2(mut nums: Vec<i32>) -> i64 {
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
    println!("{}", Solution::find_score_time_complexity_on2(vec![2,1,3,4,5,2]));
    println!("{}", Solution::find_score(vec![2,1,3,4,5,2]));
}