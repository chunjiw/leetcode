struct Solution;

impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        if s.len() == 0 {
            return true;
        }
        let mut i = 0;
        for &c in t.as_bytes() {
            if s.as_bytes()[i] == c {
                i += 1;
                if i == s.len() {
                    return true;
                }
            }
        }
        false
    }
}

fn main() {
    Solution::is_subsequence(String::new(), "abc".to_string());
}