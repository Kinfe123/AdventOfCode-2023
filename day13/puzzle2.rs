use std::fs::File;
use std::io::{self, BufRead};

fn generate(grid: &Vec<Vec<char>>) -> i32 {
    let R = grid.len();
    let C = grid[0].len();

    let mut ans = 0;
    let mut part2 = true;

    for c in 0..(C - 1) {
        let mut test = 0;

        for dc in 0..C {
            let left = c as i32 - dc as i32;
            let right = c + 1 + dc;

            if 0 <= left && left < right && right < C as i32 {
                for r in 0..R {
                    if grid[r][left as usize] != grid[r][right as usize] {
                        test += 1;
                    }
                }
            }
        }

        if test == if part2 { 1 } else { 0 } {
            ans += c as i32 + 1;
        }
    }

    for r in 0..(R - 1) {
        let mut test = 0;

        for dr in 0..R {
            let up = r as i32 - dr as i32;
            let down = r + 1 + dr;

            if 0 <= up && up < down && down < R as i32 {
                for c in 0..C {
                    if grid[up as usize][c] != grid[down as usize][c] {
                        test += 1;
                    }
                }
            }
        }

        if test == 1 {
            ans += 100 * (r as i32 + 1);
        }
    }

    ans
}

fn main() {
    let mut res = 0;
    let mut grid: Vec<Vec<char>> = Vec::new();

    if let Ok(file) = File::open("./input.txt") {
        let reader = io::BufReader::new(file);

        for line in reader.lines() {
            if let Ok(inp) = line {
                let inp = inp.replace('\n', "");

                if !inp.is_empty() {
                    grid.push(inp.chars().collect());
                } else {
                    res += generate(&grid);
                    grid.clear();
                }
            }
        }

        if !grid.is_empty() {
            res += generate(&grid);
        }

        println!("{}", res);
    }
}
