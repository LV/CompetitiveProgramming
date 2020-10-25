fn main() {
	let mut t = String::new();
	std::io::stdin().read_line(&mut t).expect("read_line error");
	let n: u32 = t.trim().parse().ok().expect("input is not an unsigned int"); // what is usize

	let mut a = 0u32;
	let mut b = 0u32;
	let mut s = String::new();
	std::io::stdin().read_line(&mut s).expect("read_line error");
	if s.chars().count() != (n as usize)+1 {
		panic!("string size does not match given int");
	}
	for i in 0..n {
		if s.chars().nth(i as usize).unwrap() == 'A' {
			a += 1
		} else if s.chars().nth(i as usize).unwrap() == 'B' {
			b += 1
		} else {
			panic!("string has a char other than 'A' or 'B'")
		}
	}

	if a > b {
		println!("A");
	} else if a < b {
		println!("B");
	} else {
		println!("Tie");
	}
}
