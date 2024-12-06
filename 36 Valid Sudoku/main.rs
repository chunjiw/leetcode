struct Solution;

impl Solution {
    pub fn is_valid(digit: char, occur: &mut Vec<i32>) -> bool {
        if let Some(num) = digit.to_digit(10) {
            let num = num as usize;
            occur[num] += 1;
            if occur[num] > 1 {
                return false;
            }
        }
        true
    }

    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut occur = vec![0; 10];
        for row in &board {
            occur.iter_mut().for_each(|x| *x = 0);
            for digit in row {
                if !Self::is_valid(*digit, &mut occur) {
                    return false;
                }
            }
        }
        for i in 0..9 {
            occur.iter_mut().for_each(|x| *x = 0);
            for j in 0..9 {
                if !Self::is_valid(board[j][i], &mut occur) {
                    return false;
                }
            }
        }
        for i in vec![0,3,6] {
            for j in vec![0,3,6] {
                occur.iter_mut().for_each(|x| *x = 0);
                for ii in vec![0,1,2] {
                    for jj in vec![0,1,2] {
                        if !Self::is_valid(board[j+jj][i+ii], &mut occur) {
                            return false;
                        }
                    }
                }

            }
        }
        true
    }
}

fn main () {
}
