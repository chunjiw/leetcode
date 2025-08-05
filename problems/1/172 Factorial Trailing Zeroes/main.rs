impl Solution {
    pub fn trailing_zeroes(n: i32) -> i32 {
        let mut count2 = 0;
        let mut count5 = 0;
        for i in 1..n+1 {
            count2 += Self::factor_count(i, 2);
            count5 += Self::factor_count(i, 5);
        }
        count2.min(count5)
    }

    fn factor_count(mut n: i32, factor: i32) -> i32 {
        let mut count = 0;
        while n > 0 && n % factor == 0 {
            n /= factor;
            count += 1;
        }
        count
    }
}