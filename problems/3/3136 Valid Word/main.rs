struct Solution;

impl Solution {
    pub fn is_valid(word: String) -> bool {
        if word.len() < 3 {
            return false;
        }
        let mut has_vowel = false;
        let mut has_consonant = false;
        for char in word.chars() {
            if !char.is_alphanumeric() {
                return false;
            }
            if "aeiouAEIOU".contains(char) {
                has_vowel = true;
            } else if char.is_alphabetic() {
                has_consonant = true;
            }
        }
        return has_vowel & has_consonant;
    }
}

fn main() {
    let s = "234Adas".to_string();
    println!("{:?}", Solution::is_valid(s));
}