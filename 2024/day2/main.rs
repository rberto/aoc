use std::fs;
use std::string;

fn islevelsafe(level : Vec<i32>) -> bool {

    let mut i = 0;
    let mut j = level.len() - 1 ;
    let mut dwok = true;
    let mut uwok = true;
    while i < (level.len() - 1)  {
        let upwalk = level[i+1] - level [i];
        let downwalk = level[j-1] - level [j];
        println!("upwalk = {upwalk}, downwalk = {downwalk}");

        match upwalk {
            1 => (),
            2 => (),
            3 => (),
            _ => {uwok = false},
        }
        match downwalk {
                1 => (),
                2 => (),
                3 => (),
                _ => {dwok =  false;},
        }

        if (uwok == false) & (dwok == false) {
            return false;
        }
        
        i += 1;
        j -= 1;    
    }
    return true;
}

fn nbofsafelevels(contents: &str) -> i32{
    let levelstr = contents.lines();

    
    let mut sum = 0;

    for level in levelstr {
        println!("level = {level}");
        let mut list1: Vec<i32> = Vec::new();
        let c: Vec<&str> = level.split(' ').collect();
        for num in c {
            list1.push(num.parse::<i32>().expect("bla1"));
        }
        if islevelsafe(list1) {
            println!("safe");
            sum += 1;
        }
    }

    return sum;
}


fn main() {

    let contents = fs::read_to_string("./input-part1.txt")
        .expect("Should have been able to read the file");

    let result = nbofsafelevels(&contents);

    println!("result = {result}");

}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let contents = fs::read_to_string("./exemple.txt")
        .expect("Should have been able to read the file");
        let result = nbofsafelevels(&contents);
        assert_eq!(result, 2);
    }
}