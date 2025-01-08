pub fn solve(input: &str) -> i16 {
    let mut floor_counter: i16 = 0;
    let mut steps: i16 = 0;

    for c in input.chars() {
        steps += 1;

        match c {
            '(' => floor_counter += 1,
            ')' => floor_counter -= 1,
            _   => {} // do nothing
        }

        if floor_counter < 0 {
            return steps
        }
    }

    -1
}

#[cfg(test)]
mod tests {
    use super::*; // Bring all the outer module's items into the scope of this module

    #[test]
    fn test_solve() {
        let test_cases = vec![
            (")", 1),
            ("()())", 5)
        ];

        for (input, expected) in test_cases {
            let function_answer = solve(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
