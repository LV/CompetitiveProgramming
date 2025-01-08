pub fn solve(input: &str) -> u32 {
    let rows: usize = 1000;
    let cols: usize = 1000;

    let mut matrix: Vec<Vec<bool>> = vec![vec![false; cols]; rows];
    for line in input.lines() {
        parse_instruction(line, &mut matrix);
    }

    // count number of lights on
    let mut counter: u32 = 0;

    for i in 0..rows {
        for j in 0..cols {
            if matrix[i][j] {
                counter += 1;
            }
        }
    }

    counter
}

fn parse_instruction(instr: &str, matrix: &mut Vec<Vec<bool>>) {
    let words: Vec<&str> = instr.split_whitespace().collect();

    if words[0] == "toggle" {
        let from: Vec<usize> = words[1].split(',').map(|w| w.parse::<usize>().unwrap()).collect();
        let to: Vec<usize> = words[3].split(',').map(|w| w.parse::<usize>().unwrap()).collect();
        toggle(from[0], from[1], to[0], to[1], matrix);
        return;
    }

    let from: Vec<usize> = words[2].split(',').map(|w| w.parse::<usize>().unwrap()).collect();
    let to: Vec<usize> = words[4].split(',').map(|w| w.parse::<usize>().unwrap()).collect();

    if words[1] == "on" {
        turn_on(from[0], from[1], to[0], to[1], matrix);
        return;
    }

    turn_off(from[0], from[1], to[0], to[1], matrix);
}

fn toggle(from_x: usize, from_y: usize, to_x: usize, to_y: usize, matrix: &mut Vec<Vec<bool>>) {
    for x in from_x..to_x+1 {
        for y in from_y..to_y+1 {
            matrix[x][y] = !matrix[x][y];
        }
    }
}

fn turn_on(from_x: usize, from_y: usize, to_x: usize, to_y: usize, matrix: &mut Vec<Vec<bool>>) {
    for x in from_x..to_x+1 {
        for y in from_y..to_y+1 {
            matrix[x][y] = true;
        }
    }
}

fn turn_off(from_x: usize, from_y: usize, to_x: usize, to_y: usize, matrix: &mut Vec<Vec<bool>>) {
    for x in from_x..to_x+1 {
        for y in from_y..to_y+1 {
            matrix[x][y] = false;
        }
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let test_cases = vec![
            ("turn on 0,0 through 999,999", 1000000),
            ("toggle 0,0 through 999,0", 1000),
            ("turn on 499,499 through 500,500", 4),
        ];

        for (input, expected) in test_cases {
            let function_answer = solve(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
