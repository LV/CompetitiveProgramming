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
