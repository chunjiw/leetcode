struct Solution;

impl Solution {
    // peak element is guaranteed to exist, so use pattern "i <= j; i = m + 1; j = m"
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let (mut i, mut j) = (0, n - 1);
        while i <= j {
            let m = (i + j) / 2;
            if (m == 0 || nums[m-1] < nums[m]) && (m == n - 1 || nums[m] > nums[m+1]) {
                return m as i32;
            } else if (m == 0 || nums[m-1] < nums[m]) && (m < n - 1 && nums[m] < nums[m+1]) {
                i = m + 1;
            } else {
                j = m;
            }
        }
        panic!("Should never reach here. Is the array not sorted?")
    }
}

fn main() {
    println!("{}", Solution::find_peak_element(vec![1,2,3,1]));
    println!("{}", Solution::find_peak_element(vec![1,2,1,3,5,6,4]));
}