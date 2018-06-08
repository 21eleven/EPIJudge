use std::env;

fn lowest_set(x : i64) -> i64 {
	// -(x - 1) - 1 is the same as
	// ~(x - 1) in python
	x & -(x - 1) - 1 
}

fn lowest_unset(x : i64) -> i64 {
	// in rust you can use ! for binary negation
	// just as you would use ~ in python
	// also: !x == -(x - 1)
	!x & (x + 1)
}

fn main() {
	let args: Vec<String> = env::args().collect();
	let input = args[1].parse::<i64>().unwrap();
	
	let lowest_set_bit = lowest_set(input);
	let lowest_unset_bit = lowest_unset(input);

	if lowest_set_bit > lowest_unset_bit {
		let output = input ^ lowest_set_bit ^ (lowest_set_bit >> 1);
		println!("{}", output);
	} else {
		let output = input ^ lowest_unset_bit ^ (lowest_unset_bit >> 1);
		println!("{}", output);
	} 

}
