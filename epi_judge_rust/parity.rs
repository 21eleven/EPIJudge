use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();
	let mut input = args[1].parse::<u64>().unwrap();
	let mut parity: u32 = 0;
	loop {
		if input  == 0u64 { break; }
		parity ^= 1;
		input &= input - 1;
	}
	/*
	let mut count = 0u32;
	loop {	
		if input >> count & 1 == 1 {
			parity ^= 1;
		}
		if input >> count == 0 {
			break;
		}
		count += 1
	}*/

	println!("{}", parity);
}
