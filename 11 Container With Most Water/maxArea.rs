impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let (mut i, mut j) = (0, height.len() - 1);
        let mut m = 0;
        while i < j {
            let a = ((j - i) as i32) * height[i].min(height[j]);
            m = m.max(a);
            if height[i] < height[j] {
                i += 1;
            } else {
                j -= 1;
            }
        }
        m
    }
}