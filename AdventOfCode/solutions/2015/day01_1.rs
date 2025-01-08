pub fn solve(input: &str) -> i16 {
    let mut counter: i16 = 0;

    for c in input.chars() {
        match c {
            '(' => counter += 1,
            ')' => counter -= 1,
            _   => {} // do nothing
        }
    }

    counter
}

#[cfg(test)]
mod tests {
    use super::*; // Bring all the outer module's items into the scope of this module

    #[test]
    fn test_solve() {
        let test_cases = vec![
            ("(())", 0),
            ("()()", 0),
            ("(((", 3),
            ("(()(()(", 3),
            ("))(((((", 3),
            ("())", -1),
            ("))(", -1),
            (")))", -3),
            (")())())", -3),
        ];

        for (input, expected) in test_cases {
            let function_answer = solve(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
