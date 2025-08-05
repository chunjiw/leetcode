impl Solution {
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        // keep a record that subarray from i to special_to[i] is special
        let mut special_to: Vec<i32> = vec![0; nums.len()];
        for (i, num) in nums.iter().enumerate() {
            if i == nums.len() - 1 || (num - nums[i+1]) % 2 == 0 {
                special_to[i] = -1;
                for j in (0..i).rev() {
                    if special_to[j] == -1 { break; }
                    special_to[j] = i as i32
                }
            }
        }
        queries.iter().map(|query|{
            query[0] == query[1] || special_to[query[0] as usize] >= query[1]
        }).collect()
    }
}