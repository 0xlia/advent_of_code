


fn main() {
    let doorid = "abbhdwsy";
    let mut password = String::new();

    let mut current_index = 0;

    while password.len() != 8 {
        let a = format!("{doorid}{}", current_index);
        let md5_hash = md5::compute(a);
        let md5_hex = format!("{:x?}", md5_hash);
        //println!("{:?}", md5_hash);
        
        //println!("{:x?}", &md5_hash.0[0..5]);


        //if &md5_hash.0[0..5] == [0,0,0,0,0] {
        if md5_hex.starts_with("00000"){
            password.push(md5_hex.chars().nth(5).unwrap() as char);
            println!("{password}");
        }
        
        current_index += 1;

    }

    println!("{password}");
}

