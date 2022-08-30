use std::env;
use std::process;

use day_1::Config;

fn main() {

    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args).unwrap_or_else(|err| {
        println!("Problem parsing args : {}", err);
        process::exit(1);
    });
    println!("program: {}", config.program_name);
    println!("file name: {}", config.file_name);
    
    if let Err(e) = day_1::run(config) {
        println!("Application error {}", e);
        process::exit(1);
    }
}

