use std::fs;
use std::io;

mod day01_1;
mod day01_2;
mod day02_1;
mod day02_2;
mod day03_1;
mod day03_2;
mod day04;
mod day05_1;
mod day05_2;
mod day06_1;
mod day06_2;

fn read_text_files_in_dir(dir_path: &str) -> io::Result<Vec<String>> {
    let mut texts = Vec::new();

    let mut entry_files: Vec<_> = fs::read_dir(dir_path)?.map(|d| d.unwrap().path()).collect();
    entry_files.sort();

    // Iterate over the entries in the given directory.
    for path in entry_files {
        // Check if the entry is a file and has a .txt extension.
        if path.is_file() && path.extension().and_then(|s| s.to_str()) == Some("txt") {
            // Read the file's contents and push it into the vector.
            let content = fs::read_to_string(path)?;
            texts.push(content);
        }
    }

    Ok(texts)
}

fn main() -> io::Result<()> {
    let file_inputs: Vec<String> = read_text_files_in_dir("/Users/luisvictoria/Dev/CompetitiveProgramming/AdventOfCode/2015/input")?;

    // collect and process arguments
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Please specify the day's puzzle to solve (e.g., 01_1 for Day 1 Part 1).");
        std::process::exit(1);
    }
    match args[1].as_str() {
        "01_1" => println!("Day 1 part 1 solution: {}", day01_1::solve(&file_inputs[1])),
        "01_2" => println!("Day 1 part 2 solution: {}", day01_2::solve(&file_inputs[1])),
        "02_1" => println!("Day 2 part 1 solution: {}", day02_1::solve(&file_inputs[2])),
        "02_2" => println!("Day 2 part 2 solution: {}", day02_2::solve(&file_inputs[2])),
        "03_1" => println!("Day 3 part 1 solution: {}", day03_1::solve(&file_inputs[3])),
        "03_2" => println!("Day 3 part 2 solution: {}", day03_2::solve(&file_inputs[3])),
        "04_1" => println!("Day 4 part 1 solution: {}", day04::solve(&file_inputs[4], 5, '0')),
        "04_2" => println!("Day 4 part 2 solution: {}", day04::solve(&file_inputs[4], 6, '0')),
        "05_1" => println!("Day 5 part 1 solution: {}", day05_1::solve(&file_inputs[5])),
        "05_2" => println!("Day 5 part 2 solution: {}", day05_2::solve(&file_inputs[5])),
        "06_1" => println!("Day 6 part 1 solution: {}", day06_1::solve(&file_inputs[6])),
        "06_2" => println!("Day 6 part 2 solution: {}", day06_2::solve(&file_inputs[6])),
        _ => eprintln!("Invalid input: {}", args[1]),
    }

    Ok(())
}
