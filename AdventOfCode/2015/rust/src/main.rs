use std::fs;
use std::io;

mod day01_1;
mod day01_2;

fn read_text_files_in_dir(dir_path: &str) -> io::Result<Vec<String>> {
    let mut texts = Vec::new();
    texts.push("stub".to_string()); // pushing stub so that inputs aren't offset by one

    // Iterate over the entries in the given directory.
    for entry in fs::read_dir(dir_path)? {
        let entry = entry?;
        let path = entry.path();

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
        _ => eprintln!("Invalid input: {}", args[1]),
    }

    Ok(())
}
