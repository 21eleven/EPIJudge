use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();
	let mut input = args[1].parse::<u64>().unwrap();
	let mut bits = 0u32;
	loop {
		if input == 0u64 { break; }
		bits += 1;
		input &= input -1;
	}

	println!("{}", bits);
}
