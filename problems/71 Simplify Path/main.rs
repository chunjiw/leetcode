struct Solution;

impl Solution {
    pub fn simplify_path(path: String) -> String {
        let parts: Vec<&str> = path.split('/').collect();
        let mut stack = vec![];
        for part in parts {
            if part.is_empty() || part == "." { continue }
            if part == ".." {
                stack.pop();
            } else {
                stack.push(part);
            }
        }
        let mut res = stack.join("/");
        res.insert(0, '/');
        res
    }
}

fn main () {
    println!("{}", Solution::simplify_path(String::from("/home/")));
    println!("{}", Solution::simplify_path(String::from("/home//foo/")));
    println!("{}", Solution::simplify_path(String::from("/home/user/Documents/../Pictures")));
    println!("{}", Solution::simplify_path(String::from("/.../a/../b/c/../d/./")));
    println!("{}", Solution::simplify_path(String::from("/../")));
}