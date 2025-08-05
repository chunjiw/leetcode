struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut i, mut j) = (0, nums.len() - 1);
        while i < j {
            let m = (i + j) / 2;
            if nums[m] < target {
                i = m + 1;
            } else if nums[m] > target {
                j = m;
            } else {
                println!("Target found within loop");
                return m as i32;
            }
        }
        return if nums[i] == target {
            println!("Target found outside of loop");
            i as i32
        } else {
            println!("Target not found but index i is at {i}");
            -1
        }
    }
}

fn main() {
    println!("target exists and is unique: {}", Solution::search(vec![-1,0,3,5,9,12], 9));
    println!("target is at left most position: {}", Solution::search(vec![-1,0,3,5,9,12], -1));
    println!("target is at right most position: {}", Solution::search(vec![-1,0,3,5,9,12], 12));
    println!("list has only one element: {}", Solution::search(vec![5], 5));
    println!("list has only two elements: {}", Solution::search(vec![5,6], 6));
    println!("target does not exist but in the middle: {}", Solution::search(vec![-1,0,3,5,9,12], 4));
    println!("target does not exist, it is out to the left: {}", Solution::search(vec![-1,0,3,5,9,12], -2));
    println!("target does not exist, it is out to the right: {}", Solution::search(vec![-1,0,3,5,9,12], 13));
}