struct Solution;

use std::collections::HashSet;

impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let count2 = Self::factor_count(n, 2);
        let count5 = Self::factor_count(n, 5);
        count2.min(count5)
    }

    fn factor_count(n: i32, factor: i32) -> i32 {
        let mut counted = HashSet::new();
        let mut count = 0;
        for i in 1..n+1 {
            if counted.contains(&i) { continue; }
            let mut count_i = 0;
            let mut y = i;
            while y <= n {
                counted.insert(y);
                count += count_i;
                y *= factor;
                count_i += 1;
            }
        }
        count
    }
}

fn main() {
    println!("3: {}", Solution::trailing_zeroes(3));
    println!("5: {}", Solution::trailing_zeroes(5));
}