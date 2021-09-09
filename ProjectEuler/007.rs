fn is_prime(i: u32, v: &Vec<u32>) -> bool {
    for x in v.iter() {
        if i % x == 0 {
            return false;
        }
    }
    return true;
}

fn main() {
    let mut vector: Vec<u32> = vec![2, 3, 5, 7, 11];
    let mut num: u32 = 13;

    while vector.len() < 10001 {
        if is_prime(num, &vector) {
            vector.push(num);
        }
        else {
            num += 2;
        }
    }

    println!("{}", vector[vector.len()-1]); // 104743
}
