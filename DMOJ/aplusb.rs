fn main() {
	let mut i1 = String::new(); // create string variable for scan
	std::io::stdin().read_line(&mut i1).expect("read_line error"); // grab input from user
	let n: i32 = i1.trim().parse().ok().expect("input is not of type int"); // convert string to int

	let mut count = 0i32; // tried to make count u32 but then it can't compare with n which is i32 lol
	loop {
		if count == n {
			break;
		} else {
			let mut s = String::new();
			std::io::stdin().read_line(&mut s).expect("read_line error"); // create second scan

			let mut parts = s.split_whitespace().map(|s| s.parse::<i32>()); // map into two different variables, split by whitespace
			match (parts.next(), parts.next()) {
				(Some(Ok(a)), Some(Ok(b))) => {
					let sum: i32 = a + b;
					println!("{}", sum);
				}
			_ => {}
			}
			count += 1;
		}
	}
}
