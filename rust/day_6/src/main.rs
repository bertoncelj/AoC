fn find_window1(input: &str, distinct: usize) -> usize {
    let mut a = 0;
    let mut b = 0;
    let mut occupied = [false; 256];
    println!("{:?}",occupied);
    let bytes = input.as_bytes();
    while b < bytes.len() && b - a < distinct {
        let c = bytes[b] as usize;
        if occupied[c] {

            occupied[bytes[a] as usize] = false;
            a +=1;
            continue;
        }
        occupied[c] = true;
        b+=1;
    }
    b
}
fn print_type<T>(_:&T)
{
    println!("{}",std::any::type_name::<T>())
}

fn find_window(input: &str, distinct: usize) -> usize {
    let r = 0; 
    let s = input.to_string();
    print_type(&s);
    for i in 0..s.len() - 3 {
        let slice = &s[i..i+4]; // get the next 4 characters
        println!("{:?}",slice);
        let mut char_set = std::collections::HashSet::new();
        for c in s.chars() {
            if char_set.contains(&c) == true && char_set.len() == 4{
                println!("{:?}",char_set);
                return i+1+4;
            }
            char_set.insert(c);
        }
    }
    3
}

fn part_one(input: &str) -> usize {
    find_window(input,4)
    // find_window1(input,4)
}

fn main() {
    println!("Hello, world!");
    let r = part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb");
    println!("{}", r);
}

mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7);
        assert_eq!(part_one("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5);

    }
}
