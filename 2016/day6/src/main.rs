use std::{collections::{BTreeMap, HashMap}, fs};

fn main() {
    // read file
    let file_content = fs::read_to_string("src/input.txt").expect("Error reading file");
    let lines = file_content.lines().filter(|s| !s.is_empty());


    // Hashmap pro position
    let mut occurrences: BTreeMap<usize, HashMap<char, usize>> = BTreeMap::new();

    // iterate over lines
    for line in lines {
        for (position, c )in line.char_indices() {
            *occurrences.entry(position)
                .or_insert_with(HashMap::new)
                .entry(c)
                .or_insert(0) += 1;
        }
    
    }

    println!("{:?}", occurrences);

    for (position, counts) in occurrences {
        let (most_common_char, _) = counts.iter()
            .min_by_key(|(_, count)| **count).unwrap();
        println!("position: {position}: {most_common_char}");
    
    }

}
