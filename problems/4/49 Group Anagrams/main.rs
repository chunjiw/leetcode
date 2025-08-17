use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map = HashMap::new();
        for str in strs {
            let mut key: Vec<char> = str.chars().collect();
            key.sort_unstable();
            let group = map.entry(key).or_insert(vec![]);
            group.push(str);
        }
        map.values().cloned().collect()
    }
}

fn main() {
    println!("{:?}", Solution::group_anagrams(vec![]));
}