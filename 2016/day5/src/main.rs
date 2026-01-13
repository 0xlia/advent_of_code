


fn main() {
    let doorid = "abbhdwsy";
    let mut password = String::new();
    let mut password2: [char; 8] = [' '; 8];

    let mut current_index = 0;

    while password2.contains(&' '){
        let a = format!("{doorid}{}", current_index);
        let md5_hash = md5::compute(a);
        let md5_hex = format!("{:x?}", md5_hash);
        //println!("{:?}", md5_hash);
        //println!("{:x?}", &md5_hash.0[0..5]);


        //if &md5_hash.0[0..5] == [0,0,0,0,0] {
        if md5_hex.starts_with("00000"){
            if password.len() != 8 {
                password.push(md5_hex.chars().nth(5).unwrap() as char);
                println!("passwort1: {password}");
            }
            
            let index_hex = md5_hex.chars().nth(5).unwrap().to_string();

            let index = usize::from_str_radix(&index_hex, 16).unwrap();

            if index <= 7 {
                let value = md5_hex.chars().nth(6).unwrap() as char;
                if password2[index] == ' ' {
                    password2[index] = value;
                }
                println!("passwort2: {:?}", password2);
            }
            
        }
        
        current_index += 1;

    }

    println!("door1: {password}");
    println!("door2: {:?}", password2);
}

