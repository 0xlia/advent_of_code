use std::fs;

enum Turn {
    L,
    R,
}
enum Direction {
    N,
    E,
    S,
    W,
}

impl Direction {
    fn next_direction(dir: &Direction, turn: &Turn) -> Direction {
        match turn {
            Turn::L => Self::counter_clockwise(dir),
            Turn::R => Self::clockwise(dir),
        }
    }

    fn clockwise(dir: &Direction) -> Direction {
        match dir {
            Direction::N => Direction::E,
            Direction::E => Direction::S, 
            Direction::S => Direction::W, 
            Direction::W => Direction::N,
        }
    }

    fn counter_clockwise(dir: &Direction) -> Direction {
        match dir {
            Direction::N => Direction::W,
            Direction::W => Direction::S, 
            Direction::S => Direction::E, 
            Direction::E => Direction::N,
        }
    }

}

fn main() {
    // parse file into vector of instructions
    let file_path = "src/input1.txt";
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    let instructions: Vec<&str> = contents.split(", ").collect();

    println!("{:?}", instructions);

    // position, direction 
    let (mut x, mut y) = (0, 0);
    let mut dir = Direction::N;

    // track locations to find easter bunny HQ
    let mut locations: Vec<(i32, i32)> = Vec::new();
    locations.push((x, y));

    // iterate over instructions vector
    for i in &instructions {
        // get turn 
        let mut turn = Turn::L;
        if i.starts_with("R") {
            turn = Turn::R
        }

        // get steps
        let mut steps_str = i.replace("L", "");
        steps_str = steps_str.replace("R", "");
        let steps = match steps_str.trim().parse::<i32>(){
            Ok(int) => int,
            Err(error)=> panic!("Problem parsing steps: {error:?}"),
        };

        // turn 
        dir = Direction::next_direction(&dir, &turn);

        // update locations
        for _ in 0..steps {
            match dir {
                // N, + y
                Direction::N => y = y + 1,
                // E, + x
                Direction::E => x = x + 1,
                // S, - y
                Direction::S => y = y - 1,
                // W, - x
                Direction::W => x = x - 1,
            };

               
            match locations.iter().find(|&&(a,b)| (a, b) == (x, y)) {
                Some(_) => {
                    println!("Easter bunny HQ: {x}, {y}, {}",x.abs() + y.abs());
                    return 
                }
                None => locations.push((x, y)),
            }
        };

        println!("current location: {x}, {y}");


    }


}
