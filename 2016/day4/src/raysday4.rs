#![allow(unused)]

#[derive(Debug)]
enum RoomError {
    // during programming, whenever we encounter a branch that leads to 
    // an error we add an enum-variant here and return it.
    MissingToken(char),
    InvalidEnd,
    NoSectorIdInHead(String),
    InvalidCharInRoomName(char),
    LessThanFiveDistinctLetters(usize),
    InvalidChecksum {
        expected: String,
        computed: String,
    }
}

fn room_check(room: &str) -> Result<(), RoomError> {
    let (head, tail) = room.split_once('[').ok_or(RoomError::MissingToken('['))?;

    // writing "" for the 2nd element checks that there is actually nothing
    // after the closing bracket ]
    let Some((expected_checksum, "")) = tail.split_once(']') else {
        return Err(RoomError::InvalidEnd)
    };

    let (name, _sector_id) = head.rsplit_once('-').ok_or(RoomError::NoSectorIdInHead(head.into()))?;

    // no hashmap, we just preallocate a vec of (char, count) pairs.
    // walking linearly through the vec is probably faster for those small strings
    let mut counters = Vec::with_capacity(room.len());

    let non_dash = |c: &char| *c != '-';

    for next in name.chars().filter(non_dash) {

        // specification says it must be lowercase
        let letter_is_valid = next.is_alphabetic() && next.is_lowercase();
        if !letter_is_valid { return Err(RoomError::InvalidCharInRoomName(next)) }

        // mutable find, so we can increment
        match counters.iter_mut().find(|(char, _)| *char == next) {
            Some((_, count)) => *count += 1,
            None => counters.push((next, 1)),
        }
    }

    use std::cmp::Ordering as Ord;
    counters.sort_by(|(char0, count0), (char1, count1)| {
        let by_count = count1.cmp(count0); // flipped to get most-first
        let lexicographic = char0.cmp(char1);

        match by_count {
            Ord::Less | Ord::Greater => by_count,
            Ord::Equal => lexicographic,
        }
    });

    // the checksum needs 5 chars according to specification, so if 
    // the room name doesn't provide those no valid checksum can be constructed
    if counters.len() < 5 {
        return Err(RoomError::LessThanFiveDistinctLetters(counters.len()))
    }

    // collect first 5 chars into `String`
    let computed_checksum = counters.iter().map(|(char, _)| *char).take(5).collect();

    match computed_checksum == expected_checksum {
        true => Ok(()),
        false => Err(RoomError::InvalidChecksum { 
            expected: expected_checksum.into(), 
            computed: computed_checksum,
        }),
    }
}

fn count_valid_rooms(input: &str) -> usize {
    input.lines().flat_map(|line| room_check(line).ok()).count()
}

fn main() {
    let input = "aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
a-b-c-123[abc]
aaaaa-bbb-z-y-x-123[abxyz
aaaaa-bbb-z-y-x-123abxyz]
aaaaa-bbb-z-y-x-123]abxyz[
aaaaa-bbb-z-y-x-123[abxyz]";

    println!("valid rooms: {}\n", count_valid_rooms(input));

    for line in input.lines() {
        println!("{line}\n  => {:?}\n\n", room_check(line));
    }
}