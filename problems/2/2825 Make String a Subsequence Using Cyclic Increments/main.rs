struct Solution;

impl Solution {
    pub fn can_make_subsequence(str1: String, str2: String) -> bool {
        let bytes1 = str1.as_bytes();
        let bytes2 = str2.as_bytes();
        let mut i = 0;
        for byte in bytes2 {
            let nextbyte = if *byte == 'a' as u8 {
                'z' as u8
            } else {
                byte - 1
            };
            let mut matched = false;
            while i < bytes1.len() {
                if bytes1[i] == *byte || bytes1[i] == nextbyte {
                    matched = true;
                    i += 1;
                    break
                }
                i += 1;
            }
            if !matched {
                return false;
            }
        }
        true
    }
}

fn main() {
    println!("{}", Solution::can_make_subsequence(String::from("abc"), String::from("ad")));
}