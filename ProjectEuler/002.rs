fn main() {
    let mut ans: u32 = 0;
    let mut prev: u32 = 1;
    let mut curr: u32 = 1;
    let mut next: u32 = 0;
    while next < 4000000 {
        next = curr + prev;
        prev = curr;
        curr = next;

        if next % 2 == 0 {
            ans += next;
        }
    }
    println!("{}", ans); // 4613732
}
