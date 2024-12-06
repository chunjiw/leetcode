struct Solution;

impl Solution {
    pub fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
        let sen = sentence.as_bytes();
        let key = search_word.as_bytes();
        let mut matching = true;
        let mut i = 0;
        let mut j = 1;
        for ch in sen {
            if *ch == 32 {
                matching = true;
                i = 0;
                j += 1;
                continue;
            }
            if matching {
                if ch != &key[i] {
                    matching = false;
                } else {
                    i += 1;
                    if i == key.len() {
                        return j;
                    }
                }
            }
        }
        -1
    }
}

fn main() {
    let sentence = String::from("i love eating burger");
    let search_word = String::from("burg");
    let res = Solution::is_prefix_of_word(sentence, search_word);
    print!("{}", res);
}