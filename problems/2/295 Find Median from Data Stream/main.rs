use std::collections::BinaryHeap;

struct MedianFinder {
    min_heap: BinaryHeap<i32>,
    max_heap: BinaryHeap<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
        MedianFinder {
            min_heap: BinaryHeap::new(),
            max_heap: BinaryHeap::new(),
        }
    }
    
    fn add_num(&mut self, num: i32) {
        if self.max_heap.is_empty() || num < *self.max_heap.peek().unwrap() {
            self.max_heap.push(num);
        } else {
            self.min_heap.push(-num);
        }
        while self.min_heap.len() > self.max_heap.len() {
            let num = -self.min_heap.pop().unwrap();
            self.max_heap.push(num);
        }
        while self.min_heap.len() + 1 < self.max_heap.len() {
            self.min_heap.push(-self.max_heap.pop().unwrap())
        }
    }
    
    fn find_median(&self) -> f64 {
        if self.max_heap.len() == self.min_heap.len() {
            ((self.max_heap.peek().unwrap() - self.min_heap.peek().unwrap()) as f64) / 2.0
        } else {
            *self.max_heap.peek().unwrap() as f64
        }
    }
}



/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */