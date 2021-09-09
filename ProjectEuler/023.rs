// This code seems like a terribly inefficient way to solve the problem, there's probably a more clever way to solve this

fn factors(i:u32) -> Vec<u32> {
    let limit: u32 = f32::sqrt(i as f32) as u32 + 1;
    let mut v: Vec<u32> = vec![1];
    
    for j in 2u32..limit {
        if i % j == 0 {
            v.push(j);
            if i/j != j {
            v.push(i/j);
            }
        }
    }
    v.sort();
    return v;
}

fn sum_factors(v: Vec<u32>) -> u32 {
    let mut sum: u32 = 0;
    for i in v.iter() {
        sum += i;
    }
    return sum;
}

fn is_abundant(i: u32) -> bool {
    return sum_factors(factors(i)) > i;
}

fn main() {
    let max: u32 = 28123;
    let mut abun: Vec<u32> = vec![];
    for i in 11u32..max+1 {
        if is_abundant(i) {
            abun.push(i)
        }
    }
    let mut abun2: Vec<u32> = vec![];
    for i in 0usize..abun.len() {
        for j in i..abun.len() {
            abun2.push(abun[i]+abun[j]);
        }
    }
    abun2.sort();
    abun2.dedup();
    abun2.reverse();
    
    let mut sum: u32 = 0;
    
    for i in 1u32..max+1 {
        if i == abun2[abun2.len()-1] {
            abun2.pop();
        } else {
            sum += i;
        }
    }
    
    println!("{}", sum); // 4179871
}
