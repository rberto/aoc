use std::fs;
use regex::Regex;


fn mulandsum(contents: &str) -> i32{
    let re = Regex::new(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)").unwrap();
    
    let mut mul: Vec<(&str, &str)> = vec![];
    for (_, [first, sec]) in re.captures_iter(contents).map(|c| c.extract()) {
        mul.push((first, sec));
    }

    println!("{:?}", mul);

    let mut result = 0;
    for m in mul {
        result += m.0.parse::<i32>().expect("should be number") * m.1.parse::<i32>().expect("should be number");
    }
    return result;
}

fn main() {

    let contents = fs::read_to_string("./input.txt")
        .expect("Should have been able to read the file");

    let result = mulandsum(&contents);

    println!("result = {result}");

}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let contents = fs::read_to_string("./exemple.txt")
        .expect("Should have been able to read the file");
        let result = mulandsum(&contents);
        assert_eq!(result, 161);
    }


}