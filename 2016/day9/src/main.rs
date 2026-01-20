use std::fs;

fn main() {

    // read file
    let file_content = fs::read_to_string("src/input.txt")
        .expect("Error reading file")
        .trim()
        .replace(" ", "");
    
    // output string
    let mut unzip: String = String::new();


    let mut i = 0;
    let file_content_vector: Vec<char> = file_content.chars().collect();
    while i < file_content.len() {
        let c = file_content_vector[i];
        // get next instuction
        if c == '(' {
            
            let slice = &file_content[i..];
            // get index ")"
            let index_instuction_end = slice.find(")").unwrap();

            // get instruction
            let instruction: Vec<&str> = slice[1..index_instuction_end].split("x").collect();
            let op1 = instruction[0].parse::<usize>().unwrap();
            let op2 = instruction[1].parse::<usize>().unwrap();

            println!("{}x{}", op1, op2);

            // get text
            let begin_text = index_instuction_end + 1;
            let end_text = begin_text + op1; 

            let text = &slice[begin_text..end_text];

            // push text op2 x
            for _ in 0..op2 {
                unzip.push_str(text);
            }

            // update i
            i += index_instuction_end + op1 +1;


            //println!("{text}");

        // push char
        } else {
            unzip.push(c);

            i += 1;
        }


    }

    let unzip = unzip.trim();
    let unzip = unzip.replace(" ", "");

    println!("{unzip}");
    println!("{}", unzip.trim().len());
    
}
