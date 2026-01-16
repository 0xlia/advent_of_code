use std::fs;
use fancy_regex::Regex;


fn main() {
    let mut tls_ips = 0;
    let mut ssl_ips = 0;

    // IPv7 supports tls
    // ABBA outside brackets
    // IABBA

    // no tls
    // ABBA inside brackets, no ABBA

    let file_content = fs::read_to_string("src/input.txt").expect("bist du dumm? gib richtigen pfad!");
    let lines = file_content.lines().filter(|s| !s.is_empty());


    // any char (.), negative lookahead (?!\1), (.), \2 repeat group2, \1 group1
    let re = Regex::new(r"(.)(?!\1)(.)\2\1").unwrap();

    // [...aba...]...bab | bab...[...aba...]
    let re2 = Regex::new(r"\[[a-z ]*(.)(?!\1)(.)\1[a-z ]*\].*\2\1\2").unwrap();

    for line in lines {
        
        let mut inside_brackets: Vec<&str> = Vec::new(); 
        let mut outside_brackets: Vec<&str> = Vec::new();  
        
        let line = line.replace("]", "[");
        let parts = line.split("[");

        // part2 
        for (i, part) in parts.enumerate() {
            if i%2 == 1 {
                inside_brackets.push(part);
            } else {
                outside_brackets.push(part);
            }
        }

        let mut inside = String::new();
        let mut outside = String::new();

        for s in inside_brackets {
            inside = format!("{inside} {s}");
        }

        for s in outside_brackets {
            outside = format!("{outside} {s}");
        }

        let input = format!("[{inside}]{outside}");
        println!("{input}");

        // part2
        if re2.is_match(&input).unwrap() {
            ssl_ips += 1;
        }



        // part1
        // let mut tls = false;
        // for (i, part) in parts.enumerate() {
        //     if re.is_match(part).unwrap() == true {
        //         if i%2 == 1 {
        //             tls = false;
        //             break;
        //         } else {
        //             tls = true;
        //         }
        //     }
        // }
        // if tls {
        //     tls_ips += 1;
        // }

    }

    println!("TLS: {tls_ips}");
    println!("SSL: {ssl_ips}");

}