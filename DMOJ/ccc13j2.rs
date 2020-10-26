fn main() {
	let mut s = String::new();
	std::io::stdin().read_line(&mut s).expect("read_line error");
	if s.chars().count() > 31 {
		panic!("String has exceeded limit")
	}
	let r_letters = ['I','O','S','H','Z','X','N'];

	let mut valid = true;


	for i in 0..s.chars().count()-1 {
		let c = s.chars().nth(i as usize).unwrap();
		let mut found = false;
		for j in 0..r_letters.len() {
			if c == r_letters[j] {
				found = true;
				break;
			}
		}
		if !found {
			valid = false;
			break;
		}
	}

	if valid {
		println!("YES");
	} else {
		println!("NO");
	}
}
