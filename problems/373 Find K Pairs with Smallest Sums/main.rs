struct Solution;

use std::{collections::BinaryHeap, vec};

impl Solution {

    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::new();
        heap.push((-nums1[0]-nums2[0], 0, 0));
        let mut result = vec![];
        for _ in 0..k {
            if let Some((_, i, j)) = heap.pop() {
                result.push(vec![nums1[i], nums2[j]]);
                if j + 1 < nums2.len() {
                    heap.push((-nums1[i]-nums2[j+1], i, j+1));
                }
                if j == 0 && i + 1 < nums1.len() {
                    heap.push((-nums1[i+1]-nums2[0], i+1, 0));
                }
            } else {
                return result;
            }
        }
        result
    }

    pub fn k_smallest_pairs0(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::new();

        for j in 0..nums2.len() {
            heap.push((-nums1[0]-nums2[j], 0, j));
        }

        let mut result = vec![];

        for _ in 0..k {
            if let Some((_, i, j)) = heap.pop() {
                result.push(vec![nums1[i], nums2[j]]);
                if i + 1 < nums1.len() {
                    heap.push((-nums1[i+1]-nums2[j], i+1, j));
                }
            } else {
                return result;
            }
        }
        result
    }
}

fn main() {
    println!("{:?}", Solution::k_smallest_pairs0(vec![1,7,11], vec![2,4,6], 3));
    println!("{:?}", Solution::k_smallest_pairs(vec![1,7,11], vec![2,4,6], 3));
}