use std::fs;

enum Direction {
    U,
    R,
    D,
    L,
}

#[derive(Debug, Clone, Copy)]
enum Key {
    K1 = 0x1,
    K2 = 0x2,
    K3 = 0x3,
    K4 = 0x4,
    K5 = 0x5,
    K6 = 0x6,
    K7 = 0x7,
    K8 = 0x8,
    K9 = 0x9,
    KA = 0xA, 
    KB = 0xB, 
    KC = 0xC, 
    KD = 0xD,
}

impl Key {
    fn next_key(key: &Key, dir: Direction) -> Key {
        match dir {
            Direction::U => {
                match key {
                    Key::K1 => Key::K1,
                    Key::K2 => Key::K2,
                    Key::K3 => Key::K1,
                    Key::K4 => Key::K4,
                    Key::K5 => Key::K5,
                    Key::K6 => Key::K2,
                    Key::K7 => Key::K3,
                    Key::K8 => Key::K4,
                    Key::K9 => Key::K9,
                    Key::KA => Key::K6,
                    Key::KB => Key::K7,
                    Key::KC => Key::K8,
                    Key::KD => Key::KB,
                }
            },
            Direction::R => {
                match key {
                    Key::K1 => Key::K1,
                    Key::K2 => Key::K3,
                    Key::K3 => Key::K4,
                    Key::K4 => Key::K4,
                    Key::K5 => Key::K6,
                    Key::K6 => Key::K7,
                    Key::K7 => Key::K8,
                    Key::K8 => Key::K9,
                    Key::K9 => Key::K9,
                    Key::KA => Key::KB,
                    Key::KB => Key::KC,
                    Key::KC => Key::KC,
                    Key::KD => Key::KD,
                }
            }
            Direction::D => {
                match key {
                    Key::K1 => Key::K3,
                    Key::K2 => Key::K6,
                    Key::K3 => Key::K7,
                    Key::K4 => Key::K8,
                    Key::K5 => Key::K5,
                    Key::K6 => Key::KA,
                    Key::K7 => Key::KB,
                    Key::K8 => Key::KC,
                    Key::K9 => Key::K9,
                    Key::KA => Key::KA,
                    Key::KB => Key::KD,
                    Key::KC => Key::KC,
                    Key::KD => Key::KD,
                }
            }
            Direction::L => {
                match key {
                    Key::K1 => Key::K1,
                    Key::K2 => Key::K2,
                    Key::K3 => Key::K2,
                    Key::K4 => Key::K3,
                    Key::K5 => Key::K5,
                    Key::K6 => Key::K5,
                    Key::K7 => Key::K6,
                    Key::K8 => Key::K7,
                    Key::K9 => Key::K8,
                    Key::KA => Key::KA,
                    Key::KB => Key::KA,
                    Key::KC => Key::KB,
                    Key::KD => Key::KD,
                }
            }
            
        }
    }
}


fn main() {
    // parse input
    let file_path = "src/input2.txt";
    let contents = fs::read_to_string(file_path).expect("error reading file");

    let instructions_iterator = contents.split("\n").filter(|s| !s.is_empty());

    //
    let mut code: u32 = 0x0u32;
    let mut current_key = Key::K5;

    for ins in instructions_iterator {
        for i in ins.chars() {
            let dir = match i {
                'U' => Direction::U,
                'L' => Direction::L,
                'D' => Direction::D,
                'R' => Direction::R,
                _ => panic!("HILFE wrong input"),
            };
            current_key = Key::next_key(&current_key, dir);
            
        }
        println!("{:?}", current_key);
        code = code * 0x10;
        println!("code: {:x}", code);
        let numberletter = current_key as u32;
        code = code + numberletter;
    }

    println!("Toilettencode: {:x}", code);


}
