pub fn solve(input: &str) -> u16 {
    let mut counter: u16 = 0;
    for line in input.lines() {
        if is_nice(line) {
            counter += 1;
        }
    }

    counter
}

fn is_nice(input: &str) -> bool {
    has_doubled_letter(input) && has_at_least_3_vowels(input) && has_no_bad_substrings(input)
}

fn has_doubled_letter(string: &str) -> bool {
    let mut prev_char: char = '?';

    for c in string.chars() {
        if c == prev_char {
            return true;
        }

        prev_char = c;
    }
    false
}

fn has_at_least_3_vowels(string: &str) -> bool {
    let mut count: u16 = 0;

    for c in string.chars() {
        if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
            count += 1
        }

        if count >= 3 {
            return true
        }
    }

    false
}

fn has_no_bad_substrings(string: &str) -> bool {
    let mut prev_char: char = '?';

    for c in string.chars() {
        if (prev_char == 'a' && c == 'b') || (prev_char == 'c' && c == 'd') || (prev_char == 'p' && c == 'q') || (prev_char == 'x' && c == 'y') {
            return false
        }

        prev_char = c;
    }

    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_nice() {
        let test_cases = vec![
            ("ugknbfddgicrmopn", true),
            ("aaa", true),
            ("jchzalrnumimnmhp", false),
            ("haegwjzuvuyypxyu", false),
            ("dvszwmarrgswjxmb", false),
        ];

        for (input, expected) in test_cases {
            let function_answer = is_nice(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
