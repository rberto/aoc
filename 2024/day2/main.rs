use std::fs;
use std::string;

fn findunsafelevel(level : Vec<i32>) -> Option<usize> {

    let ispositive = (level[1] - level [0]).is_positive();
    let mut i: usize = 0;
    while i < (level.len() - 1)  {
        let upwalk = level[i+1] - level [i];
        println!("upwalk = {upwalk}");

        if upwalk.is_positive() != ispositive {
            println!("found {i}");
            return Some(i);
        }

        match upwalk.abs() {
            1 => (),
            2 => (),
            3 => (),
            _ => {println!("found {i}"); return Some(i)},
        }
        
        i += 1;
    }
    return None;
}

fn nbunsafelevels(level : Vec<i32>) -> Option<usize> {

    let ispositive = (level[1] - level [0]).is_positive();
    let mut nb: usize = 0;
    let mut i: usize = 0;
    while i < (level.len() - 1)  {
        let upwalk = level[i+1] - level [i];
        println!("upwalk = {upwalk}");

        if upwalk.is_positive() != ispositive {
            println!("found {i}");
            nb += 1;
            i += 1;
            continue;
        }

        match upwalk.abs() {
            1 => (),
            2 => (),
            3 => (),
            _ => {println!("found {i}"); nb += 1;},
        }
        
        i += 1;
    }
    return Some(nb);
}

fn nbofsafelevels(contents: &str) -> i32{
    let levelstr = contents.lines();

    
    let mut sum = 0;

    for level in levelstr {
        println!("level = {level}");
        let c: Vec<&str> = level.split(' ').collect();

        let mut report: Vec<i32> = Vec::new();
        for num in c {
            report.push(num.parse::<i32>().expect("bla1"));
        }

        

        let nb: usize = nbunsafelevels(report.clone()).unwrap();
        println!("nb of unsafe: {nb}");

        let levels: Option<usize> = findunsafelevel(report.clone());
        if levels == None {
            println!("safe");
            sum += 1;
        } else {
            let mut copy: Vec<i32> = report.to_vec();
            copy.remove(levels.unwrap());
            println!("{:?}", copy);
            if findunsafelevel(copy) == None {
                sum += 1;
            } else {
                let mut copy2: Vec<i32> = report.to_vec();
                copy2.remove(levels.unwrap() + 1);
                println!("{:?}", copy2);
                if findunsafelevel(copy2) == None {
                    sum += 1;
                } else {
                    println!("unsafe");
                }
            }
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
        assert_eq!(result, 4);
    }

    #[test]
    fn single_level() {
        let contents = "20 22 22 23 25 29\n";
        let result = nbofsafelevels(&contents);
        assert_eq!(result, 0);
    }

    
    #[test]
    fn single_level1() {
        let contents = "57 58 59 60 64\n";
        let result = nbofsafelevels(&contents);
        assert_eq!(result, 1);
    }

}