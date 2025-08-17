impl Solution {
    pub fn is_palindrome(mut x: i32) -> bool {
        if x < 0 { return false; }
        if x == 0 { return true; }
        let mut digits = vec![];
        while x > 0 {
            digits.push(x % 10);
            x /= 10;
        }
        let (mut i, mut j) = (0, digits.len() - 1);
        while i < j {
            if digits[i] != digits[j] { return false; }
            i += 1;
            j -= 1;
        }
        true
    }
}