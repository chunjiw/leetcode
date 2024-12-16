struct Solution;

impl Solution {
    pub fn operate(operator: &str, stack: &mut Vec<i32>) {
        let (num2, num1) = (stack.pop().unwrap(), stack.pop().unwrap());
        match operator {
            "+" => stack.push(num1 + num2),
            "-" => stack.push(num1 - num2),
            "*" => stack.push(num1 * num2),
            "/" => stack.push(num1 / num2),
            _ => eprintln!("Unknown operator: {operator}")
        }
    }
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = vec![];
        for token in tokens {
            if let Ok(num) = token.parse::<i32>() {
                stack.push(num);
            } else {
                Self::operate(&token, &mut stack);
            }
        }
        stack[0]
    }
}