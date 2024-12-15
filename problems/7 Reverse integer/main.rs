struct Solution;

impl Solution {
    pub fn reverse(mut n: i32) -> i32 {
        if n == i32::MIN { return 0 }
        if n < 0 { return -Self::reverse(-n) }
        let mut stack = vec![];
        while n > 0 {
            stack.push(n % 10);
            n /= 10;
        }
        let mut result = 0;
        let sl = stack.len() as u32;
        if sl == 10 && stack[0] > 2 { return 0 }
        for (i, digit) in stack.iter().enumerate() {
            let room_left = i32::MAX - result;
            let to_add = digit * 10_i32.pow(sl - i as u32 - 1);
            if to_add > room_left { return 0 }
            result += to_add;
        }
        result
    }
}

fn main() {
    println!("{}", Solution::reverse(123));
    println!("{}", Solution::reverse(-1230));
    println!("{}", Solution::reverse(2_000_000_005));
    println!("{}", Solution::reverse(1_000_000_022));
}