fn main() {
    let max: u8 = 100;

    // Sum of square
    let mut sum_of_square: u32 = 0;
    for i in 1u32..max as u32+1 {
        sum_of_square += (i * i);
    }

    // // Square of sum
    let mut square_of_sum: u64 = 0;
    for i in 1u8..max+1 {
        square_of_sum += i as u64;
    }
    square_of_sum = square_of_sum * square_of_sum;

    println!("{}", square_of_sum-sum_of_square as u64); // 25164150
}
