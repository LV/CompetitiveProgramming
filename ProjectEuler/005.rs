fn main() {
    let max: u8 = 20;
    let mut num: u32 = max as u32;
    let mut i: u8 = 2;
    while i <= max {
        if num % i as u32 != 0 {
            num += max as u32;
            i = 2;
        } else {
            i += 1;
        }
    }
    println!("{}", num); // 232792560
}
