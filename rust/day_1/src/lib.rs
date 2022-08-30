use std::fs;
use std::error::Error;



pub fn run(config: Config) -> Result<&str, Box<dyn Error>> {

    let content = fs::read_to_string(config.file_name)?;
 
    println!("file content: {}", content);

    Ok(content)
}

pub struct Config  {
    pub  program_name: String,
    pub  file_name: String,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &str>{
        if args.len() < 2 {
            return Err("Must have 2 or more args");
        }

        let program_name = args[0].clone();
        let file_name = args[1].clone();

        Ok(Config { program_name, 
                file_name})
    }
}

pub fn search<'a>(quary: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines(){
        if line.contains(quary) {
            results.push(line);
        }
    }
    results
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
            Rust:
            safe, fast, prodactive.
            Pick tree";
        assert_eq!(vec!["safe, fast, productive"], search(query, contents));
    }



}


