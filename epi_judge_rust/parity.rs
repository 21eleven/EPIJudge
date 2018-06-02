use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();
	let input = &args[1].parse::<u64>().unwrap();
	let mut parity: u32 = 0;
	/*let mut n = input;	
	loop {
		parity ^= 1;
		let mut check = n & n - 1;
		n = &check;
		println!("{}", input);
		if n  == &0 { break; }
	}*/
	
	let mut count = 0u32;
	loop {	
		if input >> count & 1 == 1 {
			parity ^= 1;
		}
		if input >> count == 0 {
			break;
		}
		count += 1
	}
	println!("{}", parity);
}
