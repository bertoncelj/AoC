use std::fs::File;
use std::io::{Read, BufReader};

/// Generic and somewhat faster version
fn task2(data: &Vec<i32>) -> i32 
{

    let window_size = 3;
    let data_as_array = &data.as_slice();
    let mut up_count: i32 = 0;
    let mut a: i32 = data_as_array[0..window_size].iter().sum();

    for i in window_size..data.len() {
        // This is slow, we could do this better by just remembering a sum and removing the last entry
        let b = a - data_as_array[i - window_size] + data_as_array[i];
        if b > a {
            up_count += 1;
        }
        a = b;
    }

    return up_count;
}

fn task1(numbers: &Vec<i32>)-> i32
{

    let mut nn = numbers[0];
    let mut c = 0;
    for val in numbers.into_iter(){
        if  nn<*val {
            c += 1;
        }
        nn = *val;
    }

    return c;
}

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


    println!("Task 1 answ: {}", task1(&numbers));
    println!("Task 2 answ: {}", task2(&numbers));

}
