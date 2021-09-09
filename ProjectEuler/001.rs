fn main() {
    let mut ans: u32 = 0;
    for i in 0u32..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            ans += i;
        }
    }
    println!("{}", ans); // 233168
}
