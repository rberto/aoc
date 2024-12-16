use std::fs;
use std::string;

fn main() {

    let contents = fs::read_to_string("./input.txt")
        .expect("Should have been able to read the file");

    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    let couples: Vec<&str> = contents.split('\n').collect();

    for elt in couples {
        println!("{elt}\n");
        if elt.trim().len() != 0 {
            let c: Vec<&str> = elt.split(' ').collect();
            list1.push(c[0].parse::<i32>().expect("bla1"));
            list2.push(c[3].parse::<i32>().expect("bla2"));
        }
    }

    list1.sort();
    list2.sort();

    let mut i = 0;
    let mut sum = 0;

    while i < list1.len() {
        sum += (list1[i] - list2[i]).abs();
        i += 1;
    }

    println!("result is {sum}");

    // println!("With text:\n{contents}");

}