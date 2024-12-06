struct Solution;

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut i = 0;
        while i + 1 < intervals.len() {
            if intervals[i][1] >= intervals[i+1][0] {
                intervals[i][1] = intervals[i][1].max(intervals[i+1][1]);
                intervals.remove(i + 1);
            } else {
                i += 1;
            }
        }
        intervals
    }
}

fn main() {
    println!("{:?}", Solution::merge(vec![vec![1,3],vec![2,6],vec![8,10],vec![15,18]]));
}