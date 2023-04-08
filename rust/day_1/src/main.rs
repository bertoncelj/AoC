// use std::env;
// use std::process;
// use std::fs;
// use day_1::Config;

use std::fmt::Debug;

const INPUT: &str = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

struct BubbleSort;

trait TopN<T> {
    fn top_n(self, n: usize) -> Vec<T>;
}
//

impl<T: PartialOrd, U: Iterator<Item = T>> TopN<T> for U {
    fn top_n(self, n: usize) -> Vec<T> {
        // TODO: code
        let mut top = Vec::with_capacity(n);
        for value in self {
            for i in 0..n {
                if let Some(top_value) = top.get(i) {
                    if value > *top_value {
                        top[i..].rotate_right(1);
                        top[i] = value;
                        break;
                    }
                } else {
                    top.push(value);
                    break;
                }
            }
        }
        top
    }
}

fn quicksort(mut v: &mut [usize]) {
    qs(&mut v);
}

// inplace sort
fn qs(v: &mut [usize]) {
    println!("{:?}", v);

    let mid = partition(v);
    println!("mid: {}", mid);

    if v[..mid].len() > 1 {
        qs(&mut v[..mid]);
    }

    if v[mid + 1..].len() > 1 {
        qs(&mut v[mid + 1..]);
    }
}

fn partition(v_arr: &mut [usize]) -> usize {
    // chose last element as pivot

    let pivot = v_arr[0];
    let mut i: usize = 1;

    let mut j: usize = v_arr.len() - 1;
    // temporary pivot index
    loop {
        // smaller the pivot
        while i < v_arr.len() && v_arr[i] <= pivot {
            i += 1;
        }

        //bigger then pivot
        while j > 0 && v_arr[j] > pivot {
            j -= 1;
        }

        if i >= j {
            println!("In break!");
            break;
        }
        println!("{} {}", i, j);
        swap(v_arr, i, j);
        println!("{:?}", v_arr);
    }
    swap(v_arr, 0, j);
    println!("{:?}", v_arr);
    j
}

fn swap(v: &mut [usize], from: usize, to: usize) {
    let tmp = v[from];
    v[from] = v[to];
    v[to] = tmp;
}

fn main() {
    let mut v = vec![13, 14, 4, 6, 7, 10, 16, 12];

    quicksort(&mut v);
    println!("SORTED: {:?}", v);
}

// fn main() {
//
//
//     println!("Input:");
//     println!("{}", INPUT);
//     let mut max = 0;
//     let batchs = INPUT.split("\n\n");
//     for batch in batchs {
//         let lines = batch.lines();
//         let mut total = 0;
//         for line in lines {
//             println!("{}", line);
//             let value = line.parse::<u32>().unwrap();
//             total += value;
//         }
//         if total > max {
//             max = total;
//         }
//     }
//     let gucci = INPUT
//         .split("\n\n")
//         .map(|batch| {
//             batch
//                 .lines()
//                 .map(|line| line.parse::<u32>().unwrap())
//                 .sum::<u32>()
//         })
//         // assert!([1, 2, 2, 9].iter().is_sorted_by(|a, b| a.partial_cmp(b)));
//         .sort()
//         .collect::<Vec<u32>>();
//     println!("Max: {:?}", gucci);
//     println!("Max: {:?}", gucci.iter().max().unwrap());
// }
//
// fn main() {
//
//     let args: Vec<String> = env::args().collect();
//
//     let config = Config::new(&args).unwrap_or_else(|err| {
//         println!("Problem parsing args : {}", err);
//         process::exit(1);
//     });
//     println!("program: {}", config.program_name);
//     println!("file name: {}", config.file_name);
//
//     let read_file = fs::read_to_string(config.file_name)
//                 .expect("File not readable");
//
//
//     let depth_vec: Vec<u32> = read_file.lines()
//         .map(|s| s.trim().parse::<u32>()
//         .unwrap())
//         .collect();
//
//     let z = depth_vec.iter().zip(depth_vec.iter().skip(1))
//         .filter(|(x,y)| x < y)
//         .fold(0, |acc, (_x,_y)| acc + 1);
//
//     println!("Task a: {:?}", z);
//
//     let x:Vec<u32> = depth_vec.iter()
//             .zip(depth_vec.iter().skip(1))
//             .zip(depth_vec.iter().skip(2))
//             .map(|((x,y),z)| (x + y + z))
//             .collect();
//
//     let z = x.iter().zip(x.iter().skip(1))
//         .filter(|(x,y)| x < y)
//         .fold(0, |acc, (_x,_y)| acc + 1);
//
//     println!("Result of task b: {:?}", z);
// }
//
//
