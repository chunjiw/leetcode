struct Solution;

use std::collections::BinaryHeap;

impl Solution {
    pub fn find_maximized_capital(k: i32, mut w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        let n = profits.len();
        let mut available = BinaryHeap::new();
        let mut expensive = BinaryHeap::new();
        for i in 0..n {
            if capital[i] <= w {
                available.push(profits[i]);
            } else {
                expensive.push((-capital[i], profits[i]));
            }
        }
        for _ in 0..k {
            if let Some(profit) = available.pop() {
                w += profit;
                while let Some(&(cap, profit)) = expensive.peek() {
                    if -cap <= w {
                        expensive.pop();
                        available.push(profit)
                    } else {
                        break;
                    }
                }
            } else {
                return w;
            }
        }
        w
    }
}

fn main() {
    // println!("{}", Solution::find_maximized_capital(2, 0, vec![1,2,3], vec![0,1,1]));
    // println!("{}", Solution::find_maximized_capital(3, 0, vec![1,2,3], vec![0,1,2]));
    println!("{}", Solution::find_maximized_capital(3, 0, vec![1,2,3], vec![0,1,10]));
}