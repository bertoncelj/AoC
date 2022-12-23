use std::collections::HashSet;
fn get_num(input: char) -> u32 {
    let mut alphabet = ('a'..='z').into_iter().collect::<Vec<char>>();
    alphabet.append(&mut ('A'..='Z').into_iter().collect::<Vec<char>>());
    let index = alphabet.iter().position(|&x| x == input).unwrap();
    (index + 1)  as u32
}


pub fn process_part1(input: &str) -> String {
    let mut sum_score = 0;
    for line in  input.split('\n'){
        let n = line.len();
        assert_eq!(n%2, 0);
        let bag1 = &line[..n/2];
        let bag2 = &line[n/2..];
        let s1:HashSet<char> = HashSet::from_iter(bag1.chars());
        let s2:HashSet<char> = HashSet::from_iter(bag2.chars());
        for c in s1.intersection(&s2) {
            sum_score += get_num(*c);
        }
    }
    sum_score.to_string()
}

pub fn process_part2(input: &str) -> String {
    "result".to_string()
}





#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";


    #[test]
    fn part_1_it_works() {
        let result = process_part1(INPUT);
        assert_eq!(result, "157");
    }

    #[test]
    // #[ignore]
    fn part_2_it_works() {
        let result = process_part2(INPUT);
        assert_eq!(result, "70");
    }
}
