impl Solution {
    pub fn max_two_events(events: Vec<Vec<i32>>) -> i32 {
        let mut result = 0;
        for (i, event) in events.iter().enumerate() {
            result = result.max(event[2]);
            for j in i+1..events.len() {
                if event[1] < events[j][0] || events[j][1] < event[0] {
                    result = result.max(event[2] + events[j][2])
                }
            }
        }
        result
    }
}