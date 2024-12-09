impl Solution {
    pub fn my_sqrt(x: i32) -> i64 {
        if x == 0 { return 0; }
        let y = x as i64;
        let mut i: i64 = 0;
        let mut j: i64 = x as i64;
        while i < j {
            let m = i + (j - i) / 2;
            if m * m == y {
                return m;
            } else if m * m < y {
                i = m + 1;
            } else {
                j = m;
            }
        }
        if i * i == y { i } else { i - 1 }
    }
}