#[derive(Debug)]
struct LineSeg(usize, usize, usize, usize);

fn split_me(line: &str)  -> LineSeg
{
    let data: Vec<&str> = line.split(" -> ").collect();
    println!("{:?}", data);
    let point_1 = data[0];
    let point_2 = data[1];

    let xy_p1: Vec<&str> = point_1.split(",").collect();
    let xy_p2: Vec<&str> = point_2.split(",").collect();
    let x1_p1: usize = xy_p1[0].trim().parse().unwrap();
    let y1_p1: usize = xy_p1[1].trim().parse().unwrap();
    let x2_p2: usize = xy_p2[0].trim().parse().unwrap();
    let y2_p2: usize = xy_p2[1].trim().parse().unwrap();
    println!("{}", x1_p1);
    println!("{}", y1_p1);

    println!("{}", x2_p2);
    println!("{}", y2_p2);
    

    return LineSeg(x1_p1,
                   y1_p1,
                   x2_p2,
                   y2_p2 
                   );
}

fn fill_arr(arr: &mut [[usize;10];10], input: &LineSeg) {
    
    let points: Vec<(usize,usize)> = Vec::new();
    let point1: ((usize,usize), (usize,usize)) = ((0,0),(0,0));  
    let mut a = 0;
    let mut b = 0;
    let mut c = 0;
    let mut d = 0;
    let mut save = false;

    if (input.0 == input.2)  
    {
        println!("same X");
        if input.1 > input.3 {
            a = input.3;
            b = input.1;
            c = input.0;        
            d = input.0;        
        }
        else
        {
            a = input.1;
            b = input.3;
            c = input.0;        
            d = input.0;        
        }
        save = true;

    }
    else if (input.1 == input.3)
    {
        println!("same Y");
        if input.0 > input.2 {
            a = input.1;
            b = input.1;

            c = input.2;        
            d = input.0;        
        }
        else
        {
            a = input.1;
            b = input.1;

            c = input.0;        
            d = input.2;        
        }
        save = true;
    }

    if save {
        println!("a {} b{} c{} d{}", a,b,c,d);
        for row in a .. b+1 {
            for colum in c .. d+1 {
                println!("row {}, colum {}", row, colum);
                // arr[[row]colum] = 1;            
                println!("{}", arr[row][colum]);
                arr[row][colum] += 1;
            }
        }
    }

    for a in arr.iter(){
        println!("{:?}", a);
    }
    println!("{:?}", input);     
}

fn main() {

    let v1 = vec![
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
        ];
    let mut r: Vec<LineSeg> = Vec::new();
    for v in v1.iter(){
        r.push(split_me(v));
    }
    println!("{:?}", r);

    let mut arr: [[usize;10];10] = [[0;10];10];

    for vv in r.iter(){
        fill_arr(&mut arr, &vv);
    }

    for a in arr.iter(){
        println!("{:?}", a);
    }

    let mut count = 0;
    for a in arr.iter(){
        for row in a.iter(){
            if row >= &2 {
                count += 1;
            }
        }
    }
    println!("Count {}", count);

}


#[cfg(test)]
mod tests {
    #[test]

    fn it_works() {

    let v1 = vec![
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
        ];
    let mut lines: Vec<&str> = v1
        .iter()
        .map(|s| split_me(s));

    let data: Vec<&str> = v1[0]
        .split(" -> ")
        .collect();
    
    println!("{:?}", data);

    let result = 3;

    assert_eq!(result,3);
    }
}
