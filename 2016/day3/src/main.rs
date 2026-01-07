use std::fs;

fn valid_triangle(triangle: [i32; 3]) -> bool {
    return triangle[0] + triangle[1] > triangle[2]
}

fn main() {
    let mut possible_triangles = 0;

    let file_path = "src/input3.txt";
    let file_content = fs::read_to_string(file_path).expect("Error reading file");

    let lines = file_content.lines().filter(|line| !line.is_empty());

    let mut current_matrix= [[0;3];3];

    for (i, line) in lines.enumerate() {
        let triangle: Vec<i32> = line.trim().split_whitespace()
            .filter(|s| !s.is_empty())
            .map(|x| x.parse::<i32>().expect("error parsing string -> int"))
            .collect();
    
        // triangle.sort();

        //if triangle[0] + triangle[1] > triangle[2] {
        //    possible_triangles = possible_triangles + 1;
        //}

        let matrix_index = i % 3;

        current_matrix[matrix_index][0] = triangle[0];
        current_matrix[matrix_index][1] = triangle[1];
        current_matrix[matrix_index][2] = triangle[2];



        if matrix_index == 2 {
            println!("{:?}", current_matrix);


            let mut triangle0 = [current_matrix[0][0], current_matrix[1][0], current_matrix[2][0]];
            triangle0.sort();
            if valid_triangle(triangle0) {
                possible_triangles = possible_triangles + 1;
            }

            let mut triangle1 = [current_matrix[0][1], current_matrix[1][1], current_matrix[2][1]];
            triangle1.sort();
            if valid_triangle(triangle1) {
                possible_triangles = possible_triangles + 1;
            }
            
            
            let mut triangle2 = [current_matrix[0][2], current_matrix[1][2], current_matrix[2][2]];
            triangle2.sort();
            if valid_triangle(triangle2) {
                possible_triangles = possible_triangles + 1;
            }
        
        
        }
    }
           

    println!("{possible_triangles}");
}
