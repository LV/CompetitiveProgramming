extern crate md5;

pub fn solve(input: &str, digits: usize, c: char) -> u32 {
    let mut counter: u32 = 0;
    let mut curr_str: String = input.trim().to_string();
    curr_str.push_str(&counter.to_string());

    loop {
        let md5_hash: md5::Digest = md5::compute(curr_str.as_bytes());
        if check_hash(md5_hash, digits, c) {
            return counter
        }
        counter += 1;
        curr_str = input.trim().to_string();
        curr_str.push_str(&counter.to_string());
    }
}

fn check_hash(hash: md5::Digest, digits: usize, c: char) -> bool {
    let hash_str: String = format!("{:x}", hash);

    hash_str.chars().take(digits).all(|ch| ch == c)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let test_cases = vec![
            ("abcdef", 5, '0', 609043),
            ("pqrstuv", 5, '0', 1048970),
        ];

        for (input_str, input_digits, input_char, expected) in test_cases {
            let function_answer = solve(input_str, input_digits, input_char);
            assert_eq!(function_answer, expected, "Failed on input: \"{}\"; Expected: {}; Received: {}", input_str, expected, function_answer);
        }
    }
}
