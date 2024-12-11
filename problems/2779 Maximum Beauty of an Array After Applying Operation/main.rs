struct Solution;

impl Solution {
    pub fn maximum_beauty(nums: Vec<i32>, k: i32) -> i32 {
        let &m = nums.iter().max().unwrap();
        let mut count = vec![0; (m + k + 1) as usize];
        for num in nums {
            for n in num-k..num+k+1 {
                if n >= 0 {
                    count[n as usize] += 1;
                }
            }
        }
        *count.iter().max().unwrap() as i32
    }
}

fn main() {
    println!("{}", Solution::maximum_beauty(vec![4,6,1,2], 2));
    println!("{}", Solution::maximum_beauty(vec![1,1,1,1], 10));
}