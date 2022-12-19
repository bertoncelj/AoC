use std::fs;
use d1::process_part1;

fn main() {

    let input = fs::read_to_string("file1.txt").unwrap();
    println!("input_parts {:?}", process_part1(&input));

}

