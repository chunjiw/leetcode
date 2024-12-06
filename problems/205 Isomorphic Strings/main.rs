struct Solution;

use std::collections::HashMap;

impl Solution {
    
    pub fn is_isomorphic(s: String, t: String) -> bool {
        Self::is_forward_isomorphic(&s, &t) && Self::is_forward_isomorphic(&t, &s)
    }

    pub fn is_forward_isomorphic(s: &String, t: &String) -> bool {
        let mut map = HashMap::new();
        for (x, y) in s.chars().zip(t.chars()) {
            if let Some(y_) = map.get_mut(&x) {
                if y != *y_ {
                    return false;
                }
            } else {
                map.insert(x, y);
            }
        }
        true
    }
}

fn main() {
    println!("{}", Solution::is_isomorphic(String::from("badc"), String::from("baba")));
}