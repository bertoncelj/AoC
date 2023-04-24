#[derive(Debug)]
struct Student  {
    name: String,
    number: f32
}

fn main() {
    println!("Hello, world!");

    let v1: Vec<&str> = vec![
        "Tine 3.1",
        "Ana 4.4", 
        "Toni 1.2",
        "Anita 2.2",
        "Roza 9.5"
    ];
    let good: Vec<Student> = v1.iter()
        .map(|s|{
            let mut s = s.split(' ');
            let name = s.next()?.to_owned();
            let number = s.next()?.parse::<f32>().ok()?;
            
            Some(Student{name, number})
        })
        .flatten()
        .filter(|s| s.number >= 3.5)
        .collect();
    println!("good {:?}", good);
}
