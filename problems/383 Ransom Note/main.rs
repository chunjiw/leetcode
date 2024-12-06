use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut needed = HashMap::new();
        let mut count = ransom_note.len();
        for letter in ransom_note.chars() {
            let value = needed.entry(letter).or_insert(0);
            *value += 1;
        }
        for letter in magazine.chars() {
            if let Some(value) = needed.get_mut(&letter) {
                if *value > 0 {
                    count -= 1;
                    if count == 0 {
                        return true;
                    }
                }
                *value -= 1;
            }
        }
        false
    }
}

fn main() {
    println!("{}", Solution::can_construct(String::from("aa"), String::from("aab")));
}