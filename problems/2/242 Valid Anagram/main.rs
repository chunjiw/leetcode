struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map = HashMap::new();
        for ch in s.chars() {
            map.entry(ch).and_modify(|count| *count += 1).or_insert(1);
        }
        for ch in t.chars() {
            let count = map.entry(ch).and_modify(|count| *count -= 1).or_insert(-1);
            if *count < 0 {
                return false;
            }
        }
        map.values().all(|count| *count == 0)
    }
}

fn main() {
    println!("{}", Solution::is_anagram(String::from("anagram"), String::from("anagram")));
}