// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
        let (mut i, mut j) = (1, n);
        while i < j {
            let m = i + (j - i) / 2;
            if self.isBadVersion(m) {
                j = m;
            } else {
                i = m + 1;
            }
        }
        i
    }
}