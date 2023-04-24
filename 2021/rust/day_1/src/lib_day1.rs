use std::fs;

pub fn get_data()
{
    let file_content = fs::read_to_string("../deepth.txt");
    println!("{:?}", file_content );
}