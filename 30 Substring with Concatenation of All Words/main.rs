use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        let mut result = vec![];
        let mut map = HashMap::new();
        let word_len = words[0].len();
        let num_words = words.len();
        for word in words {
            let count = map.entry(word).or_insert(vec![0,0]);
            (*count).iter_mut().for_each(|x| *x += 1);
        }
        for i in 0..s.len() {
            let k = i;
            let mut matched = true;
            for j in 0..num_words {
                if k + (j+1)*word_len <= s.len() {
                    if let Some(count) = map.get_mut(&s[k+j*word_len..k+(j+1)*word_len]) {
                        if (*count)[0] > 0 {
                            (*count)[0] -= 1;
                        } else {
                            matched = false;
                            break;
                        }
                    } else {
                        matched = false;
                        break;
                    }
                } else {
                    matched = false;
                }
            }
            if matched {
                result.push(i as i32);
            }
            map.iter_mut().for_each(|(_, count)| (*count)[0] = (*count)[1]);
        }
        result
    }
}

fn main() {
    println!("{:?}", Solution::find_substring(String::from("barfoothefoobarman"), vec![String::from("foo"), String::from("bar")]));
    println!("{:?}", Solution::find_substring(String::from("wordgoodgoodgoodbestword"), vec![String::from("word"), String::from("good"), String::from("best"), String::from("word")]));
}

