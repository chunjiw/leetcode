impl Solution {
    pub fn search_range(nums: Vec<i32>, target: i32) -> Vec<i32> {
        if nums.is_empty() {
            return vec![-1, -1];
        }
        let (mut i, mut j) = (0, nums.len() - 1);
        while i < j {
            let m = i + (j - i) / 2;
            if nums[m] < target {
                i = m + 1;
            } else {
                j = m;
            }
        }
        if nums[i] != target {
            return vec![-1, -1];
        }
        let mut result: Vec<i32> = vec![i as i32];
        j = nums.len() - 1;
        while i < j {
            let m = i + (j - i) / 2;
            if nums[m] == target {
                i = m + 1;
            } else {
                j = m;
            }
        }
        if nums[i] > target {
            result.push((i - 1) as i32);
        } else {
            result.push(i as i32);
        }
        result
    }
}