use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let sb = s.as_bytes();
        let mut letters = HashSet::new();
        let mut longest = 0;
        let (mut i, mut j) = (0, 0);
        while j < s.len() {
            if letters.contains(&sb[j]) {
                while sb[i] != sb[j] {
                    letters.remove(&sb[i]);
                    i += 1;
                }
                i += 1;
            } else {
                letters.insert(&sb[j]);
                longest = if longest < letters.len() {letters.len()} else {longest};
            }
            j += 1;
        }
        longest as i32
    }
}