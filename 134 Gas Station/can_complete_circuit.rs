impl Solution {
    pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
        let n = gas.len();
        let mut net = vec![0; n];    // net gas remained after arriving next station
        for i in 0..n {
            net[i] = gas[i] - cost[i];
            if i > 0 {
                net[i] += net[i-1];
            }
        }
        if net[n-1] < 0 {
            return -1;
        }
        let mut prev = 0;
        let mut mingas = 0;
        let mut index = 0;
        for i in 0..n {
            if net[i] >= prev && prev <= mingas {
                mingas = prev;
                index = i;
            }
            prev = net[i];
        }
        index as i32
    }
}