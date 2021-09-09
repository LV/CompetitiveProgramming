fn is_palindrome(i: u32) -> bool {
    let forward: String = i.to_string();
    let backward: String = i.to_string().chars().rev().collect();
    return forward == backward;
}

fn main() {
    let mut max: u32 = 0;
    for i in 800u32..1000 {
        for j in 800u32..1000 {
            let ans: u32 = i * j;
            if ans > max && is_palindrome(ans) {
                max = ans;
            }
        }
    }
    println!("{}", max); // 906609
}
