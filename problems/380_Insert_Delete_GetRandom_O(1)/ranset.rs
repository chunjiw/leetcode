use rand::Rng;
use std::collections::HashMap;

struct RandomizedSet {
    index: HashMap<i32, usize>, // Maps values to their indices
    vals: Vec<i32>,             // Stores the values
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        RandomizedSet {
            index: HashMap::new(),
            vals: Vec::new(),
        }        
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if self.index.contains_key(&val) {
            return false;
        }
        self.index.insert(val, self.vals.len());
        self.vals.push(val);
        true        
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if let Some(&idx) = self.index.get(&val) {
            let last_val = self.vals.pop().unwrap();
            if idx != self.vals.len() {
                // Swap the value to remove with the last value
                self.vals[idx] = last_val;
                self.index.insert(last_val, idx);
            }
            self.index.remove(&val);
            true
        } else {
            false
        }        
    }
    
    fn get_random(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let i = rng.gen_range(0..self.vals.len());
        self.vals[i]        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */