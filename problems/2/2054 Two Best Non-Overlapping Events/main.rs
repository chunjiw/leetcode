impl Solution {
    pub fn max_two_events(mut events: Vec<Vec<i32>>) -> i32 {
        events.sort_unstable_by(|a, b| a[0].cmp(&b[0]));
        let n = events.len();
        let mut max_of_last = vec![0; n];
        max_of_last[n-1] = events[n-1][2];
        for k in (0..n-1).rev() {
            max_of_last[k] = max_of_last[k+1].max(events[k][2]);
        }
        let mut result = max_of_last[0];
        for (k, event) in events.iter().enumerate() {
            if k > n - 2 {
                break;
            }
            let (mut i, mut j) = (k + 1, n - 1);
            while i < j {
                let m = i + (j - i) / 2;
                if events[m][0] <= event[1] {
                    i = m + 1;
                } else {
                    j = m;
                }
            }
            if event[1] < events[i][0] {
                result = result.max(event[2] + max_of_last[i]);
            }
        }
        result
    }
}