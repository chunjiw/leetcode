impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut max1 = vec![0; n];
        let mut max2 = vec![0; n];
        // forward direction
        let mut minimum = prices[0];
        for i in 1..n {
            max1[i] = max1[i-1].max(prices[i] - minimum);
            minimum = minimum.min(prices[i]);
        }
        // backward direction
        let mut maximum = prices[n-1];
        for i in (0..n-1).rev() {
            max2[i] = max2[i+1].max(maximum - prices[i]);
            maximum = maximum.max(prices[i]);
        }
        // search for optimal combination
        let mut result = 0;
        for i in 0..n {
            result = result.max(max1[i] + max2[i]);
        }
        result
    }
}