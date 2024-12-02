use clap::{Arg, Command};

fn main() {
    let matches = Command::new("Advent of Code")
        .version("0.1.0")
        .author("Luis Victoria")
        .about("My answers to Advent of Code")
        .arg(
            Arg::new("year")
                .required(true)
                .short('y')
                .long("year")
                .value_parser(clap::value_parser!(u8))
                .help("Year the problem was released"),
        )
        .arg(
            Arg::new("question")
                .required(true)
                .short('q')
                .long("question")
                .value_parser(clap::value_parser!(u8))
                .help("Question number"),
        )
        .arg(
            Arg::new("part")
                .required(false) // Not specifying this will yield both part 1 and part 2's results
                .short('p')
                .long("part")
                .value_parser(clap::value_parser!(u8))
                .help("Part 1/2"),
        )
        .get_matches();

    let year = *matches.get_one::<u8>("year").expect("Required argument missing");
    let question = *matches.get_one::<u8>("question").expect("Required argument missing");
    let part = matches.get_one::<u8>("part").copied();
}
