struct Solution;

impl Solution {

    pub fn summary_range(range: &Vec<i32>) -> String {
        if range.len() == 1 {
            range[0].to_string()
        } else if range.len() > 1 {
            format!("{}->{}", range[0], range.last().expect("should have at least one element in range"))
        } else {
            panic!("range is empty")
        }
    }

    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut result = vec![];
        if nums.is_empty() {
            return result;
        }
        let mut prev = nums[0] - 2;
        let mut range: Vec<i32> = vec![];

        for num in nums {
            if num > prev + 1 {
                if !range.is_empty() {
                    result.push(Self::summary_range(&range));
                }
                range.clear();
            }
            range.push(num);
            prev = num;
        }
        result.push(Self::summary_range(&range));
        result
    }
}

fn main() {
    println!("{:?}", Solution::summary_ranges(vec![0,1,2,4,5,7]));
}