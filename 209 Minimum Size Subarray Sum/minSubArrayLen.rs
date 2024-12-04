struct Solution;

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let (mut i, mut j) = (0, 0);        // to consider nums[i..j]
        let mut curr_sum = 0;
        let mut min_len = usize::MAX;
        while i < nums.len() {     
            if curr_sum >= target {
                min_len = min_len.min(j - i);
                curr_sum -= nums[i];
                i += 1;
            } else if j < nums.len() {
                curr_sum += nums[j];
                j += 1;
            } else {
                break;
            }
        }
        if min_len == usize::MAX { 0 } else { min_len as i32 }
    }
}

fn main() {
    println!("{}", Solution::min_sub_array_len(7, vec![2,3,1,2,4,3]));
}