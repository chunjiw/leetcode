struct Solution;

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let mut min_index = HashMap::new();
        let mut max_index = HashMap::new();
        let mut set = HashSet::new();
        for (i, ch) in s.as_bytes().iter().enumerate() {
            min_index.entry(ch).or_insert(i);
            max_index.insert(ch, i);
        }
        let mut result = 0;
        for &ch in min_index.keys() {
            set.clear();
            for i in min_index[ch]+1..max_index[ch] {
                set.insert(s.as_bytes().get(i).unwrap());
            }
            result += set.len();
        }
        result as i32
    }
}