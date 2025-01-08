pub fn solve(input: &str) -> u32 {
    let mut count: u32 = 0;
    for line in input.lines() {
        count += calculate(line);
    }
    count
}

fn calculate(input: &str) -> u32 {
    let dimensions: Vec<&str> = input.split('x').collect();
    calculate_surface_area(dimensions[0].parse().expect("Not a number"),
                           dimensions[1].parse().expect("Not a number"),
                           dimensions[2].parse().expect("Not a number"))
}

fn calculate_surface_area(l: u32, w: u32, h: u32) -> u32 {
    let lw: u32 = l * w;
    let wh: u32 = w * h;
    let hl: u32 = h * l;

    if lw <= wh && lw <= hl {
        (l * 2) + (w * 2) + (l * w * h)
    } else if wh <= lw && wh <= hl {
        (w * 2) + (h * 2) + (l * w * h)
    } else {
        (h * 2) + (l * 2) + (l * w * h)
    }
}

#[cfg(test)]
mod tests {
    use super::*; // Bring all the outer module's items into the scope of this module

    #[test]
    fn test_solve() {
        let test_cases = vec![
            ("2x3x4", 34),
            ("1x1x10", 14),
        ];

        for (input, expected) in test_cases {
            let function_answer = solve(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
