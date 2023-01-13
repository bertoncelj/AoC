use std::{str::FromStr, string::ParseError};

#[allow(dead_code)]
#[derive(Debug)]
struct Range {
    start: u32,
    end: u32,
}

fn parse_to_vec(input: &str, na: &mut Vec<(Range, Range)>)
{
    for line in input.split('\n'){
        if line == "" {
            break
        }
        let num  = line.split(',').collect::<Vec<&str>>();
        let left = &num[0];
        let right = &num[1];


        let l = left.split('-').collect::<Vec<&str>>();
        let r = right.split('-').collect::<Vec<&str>>();
        let nnn = (Range{start:l[0].trim().parse().expect("put in number"), 
                        end:l[1].trim().parse().expect("need numbre")},
                    Range{start:r[0].trim().parse().expect("put in number"), 
                        end:r[1].trim().parse().expect("need numbre")}
        );
        na.push(nnn);
    }
}

pub fn process_part1(input:&str) -> String 
{
    let mut na: Vec<(Range,Range)> = Vec::new();
    parse_to_vec(&input, &mut na);
    let r = fully_contains(&na);
    r.to_string()
}

pub fn process_part2(input:&str) -> String {
    let mut na: Vec<(Range,Range)> = Vec::new();
    parse_to_vec(&input, &mut na);
    let r = fully_singles(&na);
    r.to_string()
}

fn fully_singles (input: &Vec<(Range,Range)>) -> u32 
{
    let mut counter:u32 = 0;
    for bag in input 
    {
        let (l,r) = bag;
        if !(l.end < r.start || r.end < l.start) 
        {
            counter += 1;
        }
    }
    counter
}

fn fully_contains (input: &Vec<(Range,Range)>) -> u32 
{
    let mut counter:u32 = 0;
    for bag in input 
    {
        let (l,r) = bag;
        if l.start <= r.start && l.end >= r.end 
        {
            counter += 1;
        }
        else if l.start >= r.start && l.end <= r.end
        {
            counter += 1;
        }
    }
    counter
}

#[cfg(test)]
mod tests {

    use super::*;
    const INPUT: &str = 
"2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"
;
    #[test]
    fn process_1_test() {
        let result = process_part1(INPUT);
        assert_eq!(result, "2");
    }

    #[test]
    fn process_2_test() {
        let result = process_part2(INPUT);
        assert_eq!(result, "4");
    }
}
