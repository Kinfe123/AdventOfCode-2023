use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let mapper: std::collections::HashMap<char, (i32, i32)> =
        [('U', (-1, 0)), ('D', (1, 0)), ('L', (0, -1)), ('R', (0, 1))]
            .iter()
            .cloned()
            .collect();

    let mut candy = vec![(0, 0)];
    let mut bars = 0;

    if let Ok(file) = File::open("./test.txt") {
        let reader = BufReader::new(file);
        for line in reader.lines() {
            if let Ok(inp) = line {
                let curr = inp.replace('\n', "");
                let parts: Vec<&str> = curr.split_whitespace().collect();
                let dxn = parts[0].chars().next().unwrap();
                let num = parts[1].parse::<i32>().unwrap();
                let color = parts[2];
                let (for_dx, for_dy) = mapper[&dxn];
                bars += num;
                let (last_r, last_c) = candy.last().unwrap();
                let moved_x = last_r + (num * for_dx);
                let moved_y = last_c + (num * for_dy);
                candy.push((moved_x, moved_y));
            }
        }
    }

    println!("{:?}", candy);

    let mut area = 0;
    for i in 0..candy.len() {
        let a = candy[i].0;
        let c = candy[(i + 1) % candy.len()].1;
        let b = if i > 0 { candy[i - 1].1 } else { 0 };
        area += a * (b - c);
    }
    let A = ((area.abs() as f32) / 2f32) as i32;

    let interior_pt = A - bars / 2 + 1;

    println!("{}", interior_pt + bars);
}
