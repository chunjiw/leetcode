struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return String::new();
        }
        let mut minlen = strs[0].len();
        for st in &strs {
            if minlen > st.len() {
                minlen = st.len();
            }
        }
        if minlen == 0 {
            return String::new();
        }
        let mut i = 0;
        while i < minlen {
            for st in &strs {
                if st.as_bytes()[i] != strs[0].as_bytes()[i] {
                    return strs[0][0..i].to_string();
                }
            }
            i += 1;
        }
        strs[0][0..i].to_string()
    }
}

fn main() {
    let strs = vec![
        String::from("flower"),
        String::from("flow"),
        String::from("flight"),
    ];
    let result = Solution::longest_common_prefix(strs);
    assert_eq!(result, "fl");
}
