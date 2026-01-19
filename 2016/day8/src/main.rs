use std::{fmt, fs};


// screen: 50wide x 6tall pixels
#[derive(Default, Debug)]
struct Screen {
    // [x][y]
    x: usize,
    y: usize,
    screen: Vec<Vec<usize>>,
}

impl fmt::Display for Screen {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut s = String::new();
        let x = self.x;
        let y = self.y;

        for j in 0..y {
            for i in 0..x {
                let mut led = ".";
                if self.screen[i][j] == 1 {
                    led = "#"
                }
                s = format!("{s}{}", led)
            }
            s = format!("{s}\n")
        }
        
        write!(f, "{s}")
    }
}

impl Screen {
    // init screen
    fn new(x: usize, y: usize) -> Screen {
        Screen {
            x: x, 
            y: y, 
            // [[0; y]; x]
            screen: vec![vec![0;y];x]
        }
    }

    // create rectange in the top-left corner
    fn rect(&mut self, x:usize, y:usize) {
        for i in 0..x as usize{
            for j in 0..y as usize{
                self.screen[i][j] = 1
            }
        }
    }

    // rotate/shift column
    fn rotate_column(&mut self, x:usize, shift:usize) {
        let old_column = &mut self.screen[x];
        let y = old_column.len();
        let mut new_column = old_column.clone();

        for i in 0..y {
            let new_index = (i + shift) % y;
            new_column[new_index] = old_column[i];
        }

        self.screen[x] = new_column.to_vec()
    }

    // rotate/shift row
    fn rotate_row(&mut self, y:usize, shift:usize) {
        // shift new row
        let mut new_row = vec![0; self.x];
        for i in 0..self.x {
            let new_index = (i + shift) % self.x;
            new_row[new_index] = self.screen[i][y] 
        }
        // insert new row
        for i in 0..self.x {
            self.screen[i][y] = new_row[i]
        }
    }

    // count lit leds 
    fn lit_led_counter(&self) -> i32{
        let mut lit = 0;
        for i in 0..self.x {
            for j in 0..self.y {
                if self.screen[i][j] == 1 {
                    lit += 1
                }
            } 
        }
        return lit
    }
}




fn main() {
    let mut screen = Screen::new(50, 6);

    let file_content = fs::read_to_string("src/input.txt").expect("Lies doch richig!");
    for line in file_content.lines().filter(|s| !s.is_empty()) {
        let instruction: Vec<&str> = line.split(" ").collect(); 
        println!("{:?}", instruction);
        match instruction[0] {
            // call rect function
            "rect" => {
                let xy: Vec<&str> = instruction[1].split("x").collect();
                let x = xy[0].parse::<usize>().unwrap();
                let y = xy[1].parse::<usize>().unwrap();
                screen.rect(x, y);
            },
            // call rotate function
            "rotate" => {
                let rotation: Vec<&str> = instruction[2].split("=").collect();
                let cow = rotation[1].parse::<usize>().unwrap();
                let shift = instruction[4].parse::<usize>().unwrap();

                match rotation[0] {
                    "x" => {screen.rotate_column(cow, shift);},
                    "y" => {screen.rotate_row(cow, shift);},
                    _ => panic!("rotation failed")
                }
            },
            _ => panic!("parsing file failed")
        }

        println!("{screen}");
    }

    println!("lit leds: {}", screen.lit_led_counter());

    // let mut leds = Screen::new(7, 3);
    // leds.rect(3, 2);

    // println!("{}", leds);

    // leds.rotate_column(1, 1);

    // println!("{}", leds);

    // leds.rotate_row(0, 4);

    // println!("{}", leds);


    // println!("lit leds: {}", leds.lit_led_counter())
}
