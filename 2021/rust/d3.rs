use std::fs::File;
use std::io::{Read, BufReader};
use std::convert::TryInto;
use std::any::type_name;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}

fn most_occur_bit_column(data: &Vec<&str>,bit_pos: usize) -> u8 
{
    let len_inputs = data.len();

    let mut count_1 = 0;
    let mut count_0 = 0;

    for input_pos in 0..len_inputs 
    {
        let bits_str = data[input_pos];
        let bit = &bits_str.chars().nth(bit_pos).unwrap();

        match bit {
            '1' => {
                count_1 += 1;
            }
            '0' => {
                count_0 += 1;
            }
            _ => {
                println!("Erorr");
            }
        }
    }
    if count_0 <= count_1 {
        return 1;
    } else {
        return 0;
    }
}

fn task1(data: &Vec<&str>) -> i64
{
    
    let len_bits = data[0].len();
    let len_inputs = data.len();


    let mut bit_seq: Vec<u8> = Vec::new();

    for bit_pos in 0..len_bits {
        let most_occur_bit = most_occur_bit_column(&data, bit_pos.try_into().unwrap());
        bit_seq.push(most_occur_bit);
    }

    let binary_str: String = bit_seq.into_iter().map(|i| i.to_string()).collect::<String>();
    let binary: i64 = i64::from_str_radix(&binary_str, 2).unwrap();

    return binary;
}

fn get_oxygen(data: &Vec<&str>) -> i64
{
    let mut v: Vec<&str> = Vec::new();
    for d in data.iter()
    {
        v.push(d);
    }

    for nth_bit in 0..data[0].len()
    {
        let popular_bit = most_occur_bit_column(&v, nth_bit);
        v.retain(|&x| popular_bit.to_string().eq(&x.chars().nth(nth_bit).unwrap().to_string()));
        if v.len() == 1
        {
            break;
        }

    }

    let binary_str: String = v.into_iter().map(|i| i.to_string()).collect::<String>();
    let binary: i64 = i64::from_str_radix(&binary_str, 2).unwrap();

    return binary;
}

fn get_co2(data: &Vec<&str>) -> i64
{
    let mut v: Vec<&str> = Vec::new();
    for d in data.iter()
    {
        v.push(d);
    }

    for nth_bit in 0..data[0].len()
    {
        let popular_bit = most_occur_bit_column(&v, nth_bit);
        v.retain(|&x| !popular_bit.to_string().eq(&x.chars().nth(nth_bit).unwrap().to_string()));
        if v.len() == 1
        {
            break;
        }

    }

    let binary_str: String = v.into_iter().map(|i| i.to_string()).collect::<String>();
    let binary: i64 = i64::from_str_radix(&binary_str, 2).unwrap();

    return binary;
}


fn task2(data: &Vec<&str>) -> i64
{
    let oxygen = get_oxygen(&data);
    let co2 = get_co2(&data);

    return oxygen * co2;
}

fn main() {

#[warn(non_snake_case)]
    let mut input_string = String::new();
    let file = File::open("bits.txt").expect("Error in reading file");
    let mut buffer_reader = BufReader::new(file);
    buffer_reader.read_to_string(&mut input_string).expect("Unable to read line");

    let commands = input_string;
    let input_vec = commands.split("\r\n").collect::<Vec<&str>>();

    // remove empty spaces
    let data = input_vec.into_iter().filter(|&i| !i.is_empty()).collect::<Vec<&str>>();
    println!("Result task1: {}", task1(&data));
    println!("Result task2: {}", task2(&data));
  
}





