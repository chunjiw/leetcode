struct Solution;

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut result = vec![];
        if intervals.is_empty() {
            return result;
        }
        intervals.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
        let mut current = intervals[0].clone();
        for (i, range) in intervals.iter().enumerate() {
            if current[1] < range[0] {
                result.push(current.clone());
                current[0] = range[0];
                current[1] = range[1];
            } else {
                current[1] = current[1].max(range[1]);
            }
            if i == intervals.len() - 1 {
                result.push(current.clone());
            }
        }
        result
    }
}

fn main() {
    println!("{:?}", Solution::merge(vec![vec![1,3],vec![2,6],vec![8,10],vec![15,18]]));
}