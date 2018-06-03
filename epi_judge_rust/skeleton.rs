use std::env;

fn main() {
	let args: Vec<String> = env::args().collect();
	let input = args[1].parse::<u64>().unwrap();

	println!("{}", output);
}
