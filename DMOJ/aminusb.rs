fn main() {
	let mut i1 = String::new(); // create string variable for scan
	std::io::stdin().read_line(&mut i1).expect("read_line error"); // grab input from user
	let n: i32 = i1.trim().parse().ok().expect("input is not of type int"); // convert string to int

	for _ in 0..n {
		let mut s = String::new();
		std::io::stdin().read_line(&mut s).expect("read_line error"); // create second scan

		let mut parts = s.split_whitespace().map(|s| s.parse::<i32>().unwrap());
		let a = parts.next().unwrap();
		let b = parts.next().unwrap();
		println!("{}", a - b);
	}
}
