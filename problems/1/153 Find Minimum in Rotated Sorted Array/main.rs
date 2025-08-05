struct Solution;

impl Solution {
    // minimum is guaranteed to exist, so use pattern "i <= j; i = m + 1; j = m"
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let (mut i, mut j) = (0, n - 1);
        while i <= j {
            let m = (i + j) / 2;
            if nums[i] < nums[j] || i == j {
                return nums[i];
            }
            if i == m {
                return nums[i].min(nums[j]);
            }
            if nums[i] < nums[m] && nums[m] > nums[j] {
                i = m + 1;
            } else {
                j = m;
            }
        }
        panic!("Should not reach here");
    }
}

fn main() {
    println!("{}", Solution::find_min(vec![]));
}