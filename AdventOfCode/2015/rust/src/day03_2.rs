use std::collections::HashSet;

pub fn solve(input: &str) -> u16 {
    let mut counter: u16 = 1; // start at 1 because (0,0) is already visited
    let mut is_santa: bool = true;
    let mut x_santa: i16 = 0;
    let mut x_robo:  i16 = 0;
    let mut y_santa: i16 = 0;
    let mut y_robo:  i16 = 0;
    let mut visited: HashSet<(i16, i16)> = HashSet::new();
    visited.insert((0, 0));
    for c in input.chars() {
        match c {
            '^' => {
                if is_santa {
                    y_santa += 1
                } else {
                    y_robo += 1
                }
            },
            'v' => {
                if is_santa {
                    y_santa -= 1
                } else {
                    y_robo -= 1
                }
            },
            '<' => {
                if is_santa {
                    x_santa -= 1
                } else {
                    x_robo -= 1
                }
            },
            '>' => {
                if is_santa {
                    x_santa += 1
                } else {
                    x_robo += 1
                }
            },
            _   => eprintln!("Invalid char: {}", c),
        }

        let x: i16;
        let y: i16;

        if is_santa {
            x = x_santa;
            y = y_santa;
        } else {
            x = x_robo;
            y = y_robo;
        }
        let curr_coordinate: (i16, i16) = (x, y);
        if !visited.contains(&curr_coordinate) {
            counter += 1;
            visited.insert(curr_coordinate);
        }

        is_santa = !is_santa
    }
    counter
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let test_cases = vec![
            ("^v", 3),
            ("^>v<", 3),
            ("^v^v^v^v^v", 11),
        ];

        for (input, expected) in test_cases {
            let function_answer = solve(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
