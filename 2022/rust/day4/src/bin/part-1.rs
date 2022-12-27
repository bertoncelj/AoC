use day4::process_part1;
use std::fs;

fn main(){

    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", process_part1(&file));

    // let ex: &str = "neki";
    // let exx: String = String::from("Partner");

    // let some:String = "slive".to_string();

    // let str_from_string: &str = &exx;

    // let combine = ["first", "second"].concat();

    // let mut mut_string = String::new();
    // mut_string.push_str("neki");
    // mut_string.push('a');
    // mut_string.push('b');

    // let a = String::from("aadad");
    // let b = String::from("a");
    // let stra: &str = &a[1..2];
    // dbg!(stra);
    

    // let Some(char_by_index) = &ex.chars().nth(1);
    // dbg!(char_by_index);

    // match char_by_index {
    //     Some(c) => println!("found a char {}", c),
    //     None => {}
    // }
   
    // let mut a = 22;
    // let b = a;
    // let c = b;
    // println!("{}",b);
    // println!("{}",c);
    // dbg!(a);
    // let vec_i: Vec<u32> = Vec::new();
    // let string_a: String = String::from("hello!");

    // let heap_i8: Box<i8> = Box::new(39);
    // let aa = a;
    // println!("{}",a);
    // println!("{}",aa);
    
    // let v = vec_i.clone();
    // let vv = &vec_i;
    // println!("{:?}",vec_i);
    // println!("{:?}",vv);
    // println!("{:?}",v);
    // stack_neki(&mut a);
    // let ha = heap_memory(&vec_i);
    // println!("{}", a);
    // println!("{:?}", ha);


    // let some_string: String = String::from("Howday!");
    // let some_str: &str = "hihi";
    // string_print(&some_string, &some_str);

    // println!("{} {}", some_string, some_str);



    // let var_1 = jaja {a:10, b:3.14};
    // print_struct(var_1);
    // println!("{:?}", var_1);

}

fn print_struct(a: jaja)
{
    println!("{:?}", a);
}

#[derive(Debug, Clone, Copy)]
struct jaja {
    a: u32,
    b: f32,
}

fn string_print(a: &String, b: &str)
{
    println!("{} {}", a, b);
}

fn stack_neki(a: &mut u32)
{
    *a += 1;
    println!("{}", a);
}

fn heap_memory(a: &Vec<u32>) -> Vec<u32>
{
    println!("{:?}", a);
    a.to_vec()
}
