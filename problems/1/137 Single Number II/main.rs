struct Solution;

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut bits = vec![0; 32];
        for n in nums {
            for i in 0..32 {
                bits[i] += (n >> i) & 1;
            }
        }
        let mut result = 0;
        for (i, b) in bits.iter().enumerate() {
            if b % 3 == 0 { continue }
            result |= 1 << i;
        }
        result
    }
}

fn main() {
    println!("{}", Solution::single_number(vec![2,2,3,2]));
    println!("{}", Solution::single_number(vec![-2,-2,3,-2]));
    println!("{}", Solution::single_number(vec![-2,-2,-3,-2]));
}