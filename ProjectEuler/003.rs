fn main() {
    let mut num: u64 = 600851475143;
    let limit: u64 = f64::sqrt(num as f64) as u64 + 1;
    let mut i: u64 = 3;
    let mut vector: Vec<u64> = vec![];

    while i < limit {
        if num % 2 == 0 {
            vector.push(2);
            num /= 2;
        } else if num % i == 0 {
            vector.push(i);
            num /= i;
            i = 3;
        } else {
            i += 2;
        }
    }

    vector.sort();
    println!("{}", vector[vector.len()-1]); // 6857
}
