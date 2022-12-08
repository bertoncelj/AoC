

fn main() {

    let input = std::fs::read_to_string("file1.txt").unwrap();

    println!("input_parts {:?}", input);

    // let a: Vec<u32> = input
    // .split("\n\n")
    // .map(|s| s.parse::<u32>().ok())
    // .collect();

    // let a: Vec<u32> = input
    //     // .unwrap()
    //     // .split("\n\n")
    //     .lines()
    //     .map(|p| p.parse::<u32>().unwrap())
    //     .collect();
    
    let a: Vec<&str> = input
        .lines()


        
    // let mut input_parts = input
    //             .split("\n\n")
    //             .unwrap();


    println!("input_parts {:?}", a);

    // let numbers: Vec<usize> = input_parts
    //     .next()
    //     .unwrap()
    //     .split(',')
    //     .map(|p| p.parse::<usize>().unwrap())
    //     .collect();


    // println!("numbers {:?}", numbers);
    // println!(" {:?}", input_parts);


    // let a = include_str!("../file1.txt")
    //                 .lines()
    //                 .map(|n| n.parse().unwrap())
    //                 .collect::<Vec<u16>>();
    // println!("{:?}",a);
                    

}

