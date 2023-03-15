fn find_window(input: &str, distinct: usize) -> usize {
    let mut a = 0;
    let mut b = 0;
    let mut occupied = [false; 256];

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

fn part_one(input: &str) -> usize {
    find_window(input,4)
}

fn main() {
    println!("Hello, world!");
}

mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7);
        assert_eq!(part_one("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5);

    }
}
