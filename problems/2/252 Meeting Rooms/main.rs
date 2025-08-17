impl Solution {
    pub fn can_attend_meetings(mut intervals: Vec<Vec<i32>>) -> bool {
        intervals.sort();
        let n = intervals.len();
        if n == 0 {
            return true;
        }
        for i in 0..(n-1) {
            if intervals[i][1] > intervals[i+1][0] {
                return false;
            }
        }
        return true;
    }
}
