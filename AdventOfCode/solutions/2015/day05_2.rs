use std::collections::HashSet;

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
    has_pair_appearing_twice(input) && has_one_letter_repeating_between(input)
}

// This two letter pair must appear at least twice in the string without overlapping
fn has_pair_appearing_twice(s: &str) -> bool {
    let chars: Vec<char> = s.chars().collect();
    let mut visited: HashSet<(char, char)> = HashSet::new();
    let mut prev_pair: (char, char) = ('?', '!');

    for i in 1..chars.len() {
        let curr_pair: (char, char) = (chars[i-1], chars[i]);
        if !(visited.contains(&curr_pair)) {
            visited.insert(curr_pair);
            prev_pair = curr_pair;
            continue;
        }

        if curr_pair == prev_pair {
            prev_pair = ('?', '!');
            continue;
        }

        return true;
    }

    false
}

fn has_one_letter_repeating_between(string: &str) -> bool {
    let mut first: char = '?';
    let mut second: char = '!';

    for c in string.chars() {
        if first == c {
            return true;
        }

        first = second;
        second = c;
    }

    false
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_has_pair_appearing_twice() {
        let test_cases = vec![
            ("xyxy", true),
            ("aabcdefgaa", true),
            ("aaa", false),
        ];

        for (input, expected) in test_cases {
            let function_answer = has_pair_appearing_twice(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }

    #[test]
    fn test_has_one_letter_repeating_between() {
        let test_cases = vec![
            ("xyx", true),
            ("abcdefeghi", true),
            ("aaa", true),
        ];

        for (input, expected) in test_cases {
            let function_answer = has_one_letter_repeating_between(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }

    #[test]
    fn test_is_nice() {
        let test_cases = vec![
            ("qjhvhtzxzqqjkmpb", true),
            ("xxyxx", true),
            ("uurcxstgmygtbstg", false),
            ("ieodomkazucvgmuy", false),
        ];

        for (input, expected) in test_cases {
            let function_answer = is_nice(input);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input, expected, function_answer);
        }
    }
}
