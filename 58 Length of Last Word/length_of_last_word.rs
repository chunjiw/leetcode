impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut counting = false;
        let mut result = 0;
        for c in s.chars().rev() {
            if c == ' ' {
                if counting {
                    break;
                } else {
                    continue;
                }
            } else {
                counting = true;
                result += 1;
            }
        }
        result
    }
}