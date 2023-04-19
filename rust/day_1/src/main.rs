use std::env;
use std::process;
use std::fs;

fn get_data(file_name: &str)
{
    let file_content = fs::read_to_string(file_name).unwrap();
    let string_array: Vec<&str> = file_content.lines().collect::<Vec<&str>>();
    println!("{:?}", string_array );
    let int_vec: Vec<u32> = string_array
    .iter()
    .map(|s| s.parse().unwrap())
    .collect();
    println!("{:?}", int_vec );

}

fn main() {

    get_data("../deepth.txt")
}

// fn main() {

//     let args: Vec<String> = env::args().collect();

//     let config = Config::new(&args).unwrap_or_else(|err| {
//         println!("Problem parsing args : {}", err);
//         process::exit(1);
//     });
//     println!("program: {}", config.program_name);
//     println!("file name: {}", config.file_name);
    
//     let read_file = fs::read_to_string(config.file_name)
//                 .expect("File not readable");


//     let depth_vec: Vec<u32> = read_file.lines()
//         .map(|s| s.trim().parse::<u32>()
//         .unwrap())
//         .collect();
    
//     let z = depth_vec.iter().zip(depth_vec.iter().skip(1))
//         .filter(|(x,y)| x < y)
//         .fold(0, |acc, (_x,_y)| acc + 1);

//     println!("Task a: {:?}", z);

//     let x:Vec<u32> = depth_vec.iter()
//             .zip(depth_vec.iter().skip(1))
//             .zip(depth_vec.iter().skip(2))
//             .map(|((x,y),z)| (x + y + z))
//             .collect();
    
//     let z = x.iter().zip(x.iter().skip(1))
//         .filter(|(x,y)| x < y)
//         .fold(0, |acc, (_x,_y)| acc + 1);

//     println!("Result of task b: {:?}", z);
// }


