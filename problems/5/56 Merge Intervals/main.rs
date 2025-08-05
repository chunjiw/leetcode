struct Solution;

impl Solution {

    pub fn merge_in_place(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if intervals.is_empty() {
            return intervals;
        }
        intervals.sort_unstable_by(|a, b| a[1].cmp(&b[1]));
        let n = intervals.len();
        let mut j = n - 1;    // i: to be merged; j: to be merged to
        for i in (0..n-1).rev() {
            if intervals[i][1] < intervals[j][0] {
                j -= 1;
                // copy i to j as the new range to be merged to
                intervals[j][0] = intervals[i][0];
                intervals[j][1] = intervals[i][1];
            } else {
                intervals[j][0] = intervals[j][0].min(intervals[i][0]);
            }
        }
        intervals[j..n].to_vec()
    }

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
    println!("{:?}", Solution::merge_in_place(vec![vec![1,3],vec![2,6],vec![8,10],vec![15,18]]));
    println!("{:?}", Solution::merge(vec![vec![1,3],vec![2,6],vec![8,10],vec![15,18]]));
}