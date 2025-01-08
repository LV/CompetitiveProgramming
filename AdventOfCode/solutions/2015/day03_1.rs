use std::collections::HashSet;

pub fn solve(input: &str) -> u16 {
    let mut counter: u16 = 1; // start at 1 because (0,0) is already visited
    let mut x: i16 = 0;
    let mut y: i16 = 0;
    let mut visited: HashSet<(i16, i16)> = HashSet::new();
    visited.insert((0, 0));
    for c in input.chars() {
        match c {
            '^' => y += 1,
            'v' => y -= 1,
            '<' => x -= 1,
            '>' => x += 1,
            _   => eprintln!("Invalid char: {}", c),
        }

        let curr_coordinate: (i16, i16) = (x, y);
        if !visited.contains(&curr_coordinate) {
            counter += 1;
            visited.insert(curr_coordinate);
        }
    }
    counter
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let test_cases = vec![
            (">", 2),
            ("^>v<", 4),
            ("^v^v^v^v^v", 2),
        ];

        for (input, expected) in test_cases {
            let function_answer = solve(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
