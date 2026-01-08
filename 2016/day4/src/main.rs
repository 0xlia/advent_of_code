use std::{cmp::Ordering, collections::HashMap, fs};

#[derive(Debug, Eq, PartialEq)]
struct Letter {
    letter: char,
    count: i32,
}

impl Ord for Letter {
   fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.count.cmp(&other.count) == Ordering::Equal {
            self.letter.cmp(&other.letter)
        } else {
            other.count.cmp(&self.count)
        }
   }
}

impl PartialOrd for Letter {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}


fn main() {
    let mut result = 0;


    // parse file
    let file_content = fs::read_to_string("src/input4.txt").expect("Unable to read file");
    let lines = file_content.lines().filter(|s| !s.is_empty());

    for line in lines {
        // extract checksum, roomname, roomnumber
        let (a, checksum) = line.trim().split_once("[").unwrap();
        let (roomname, roomnumber) = a.rsplit_once("-").unwrap();
        let roomname = roomname.replace("-", "");
        let roomnumber = roomnumber.parse::<i32>().unwrap();
        let checksum = checksum.replace("]", "");

        // count letters
        let mut letters: HashMap<char, i32> = HashMap::new();
        for letter in roomname.chars() {
            let count = letters.entry(letter).or_insert(0);
            *count += 1;
        }

        let mut letters_vec: Vec<Letter> = Vec::new();

        for (letter, count) in letters.into_iter() {
            let new_letter = Letter { letter, count};
            letters_vec.push(new_letter);
        }

        letters_vec.sort();

        let mut letters_checksum = String::new();
        letters_checksum.push(letters_vec[0].letter);
        letters_checksum.push(letters_vec[1].letter);
        letters_checksum.push(letters_vec[2].letter);
        letters_checksum.push(letters_vec[3].letter);
        letters_checksum.push(letters_vec[4].letter);

        println!("name: {roomname}, number: {roomnumber}, checksum {checksum}, our checksum {letters_checksum}");

        if letters_checksum == checksum {
            result += roomnumber;
        }
        
    }

    println!("{result}");

}
