struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut i, mut j) = (0, nums.len() - 1);
        while i < j {
            let m = i + (j - i) / 2;
            if nums[m] == target {
                return m as i32;
            }
            if (nums[i] < nums[j] && nums[m] < target)
            || (i == m)
            || (nums[i] > nums[j] && nums[i] < nums[m] && nums[m] < target)
            || (nums[i] > nums[j] && nums[i] < nums[m] && target <= nums[j])
            || (nums[i] > nums[j] && nums[m] < target && target <= nums[j]) {
                i = m + 1;
            } else {
                j = m;
            }
        }
        if nums[i] == target { i as i32 } else { -1 }
    }
}

fn main() {
    println!("{}", Solution::search(vec![4,5,6,7,0,1,2], 0));
    println!("{}", Solution::search(vec![4,5,6,7,0,1,2], 1));
    println!("{}", Solution::search(vec![4,5,6,7,0,1,2], 6));
    println!("{}", Solution::search(vec![4,5,6,7,0,1,2], 3));
    println!("{}", Solution::search(vec![1], 0));
}