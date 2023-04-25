use std::fs::File;
use std::io::{Read, BufReader};

fn task1(data: &Vec<&str>) -> (i64,i64)
{
    let mut horizontal:i64 = 0;
    let mut vertical:i64 = 0;

    for command in data.into_iter()
    {
        if !command.is_empty(){
            let comm = command.split(" ").collect::<Vec<&str>>();
            let comm_num:i64 = comm[1].parse().unwrap();
            let comm_str = comm[0];

            match comm_str {
                "forward" => {
                    horizontal += comm_num;
                }
                "down" => {
                    vertical += comm_num;
                }
                "up" => {
                    vertical -= comm_num;
                }
                _ => {
                    println!("Error! Parse failed");
                }
            }
        }

    }

    (horizontal,vertical)
}

fn task2(data: &Vec<&str>) -> (i64,i64)
{
    let mut horizontal:i64 = 0;
    let mut depth:i64 = 0;
    let mut aim:i64 = 0;

    for command in data.into_iter()
    {
        if !command.is_empty(){
            let comm = command.split(" ").collect::<Vec<&str>>();
            let comm_num:i64 = comm[1].parse().unwrap();
            let comm_str = comm[0];

            match comm_str {
                "forward" => {
                    horizontal += comm_num;
                    depth += aim*comm_num;
                }
                "down" => {
                    aim += comm_num;
                }
                "up" => {
                    aim -= comm_num;
                }
                _ => {
                    println!("Error! Parse failed");
                }
            }
        }

    }

    (horizontal,depth)
}

fn main() {

#[warn(non_snake_case)]
    let mut input_string = String::new();
    let file = File::open("path.txt").expect("Error in reading file");
    let mut buffer_reader = BufReader::new(file);
    buffer_reader.read_to_string(&mut input_string).expect("Unable to read line");

    let commands = input_string;
    let input_vec = commands.split("\r\n").collect::<Vec<&str>>();

    let (horizontal,vertical) = task1(&input_vec); 

    println!("Horizontal: {} Vertical: {}", horizontal, vertical);
    println!("Task1 multy: {}", horizontal*vertical);
    println!("");

    let (horizontal,vertical) = task2(&input_vec); 

    println!("Horizontal: {} Vertical: {}", horizontal, vertical);
    println!("Task2 multy: {}", horizontal*vertical);

}

