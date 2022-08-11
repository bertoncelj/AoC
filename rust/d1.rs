use std::fs::File;
use std::io::{Read, BufReader};

fn main() {
    let mut neki = String::new();
    let file = File::open("deepth.txt").expect("Error in reading file");
    let mut bufferReader = BufReader::new(file);
    bufferReader.read_to_string(&mut neki).expect("Unable to read line");

    let mut numbers = neki;

    let numbers: Vec<i32> = numbers
        .split_whitespace()
        .map(|s| s.parse().expect("parse error"))
        .collect();

    let mut nn = numbers[0];
    let mut c = 0;
    for val in numbers.into_iter(){
        if  nn<val {
            c += 1;
        }
        nn = val;
    }
    println!("{}", c);
}
