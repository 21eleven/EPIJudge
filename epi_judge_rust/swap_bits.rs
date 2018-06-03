use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();
	let mut n = args[1].parse::<u64>().unwrap();
	let idx1 = args[2].parse::<u64>().unwrap();
	let idx2 = args[3].parse::<u64>().unwrap();

	if (n >> idx1 & 1) != (n >> idx2 & 1) {
		n = n ^ (1 << idx1) ^ ( 1 << idx2);
	}

	println!("{}", n);
}
