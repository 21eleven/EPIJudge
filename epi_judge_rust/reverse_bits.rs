use std::env;
use std::collections::HashMap;

fn reverse_i64_bits(x : i64) -> i64 {
	let mut y: i64 = x;
	for i in 0..8 {
		if ((x >> i) & 1) != ((x >> 15-i) & 1) {
			y ^= (1 << i) ^ (1 << 15 - i);
		}
	}
	return y
}

	

fn init_lookup() -> HashMap<i64, i64> {
	let mut map : HashMap<i64, i64> = HashMap::with_capacity(65536);

	//for n in 0..6 {
	for n in 0..65536 {
		let r : i64 = reverse_i64_bits(n);
		map.insert(n, r);
	}
	return map
}

fn main() {
	let args: Vec<String> = env::args().collect();
	//let input = args[1].parse::<i64>().unwrap();
	let input = args[1].parse::<u64>().unwrap();
	//let output = reverse_i64_bits(input);
	let reversals = init_lookup();

	let part_one : i64 = (input & 0xffff) as i64;
	let part_two : i64 = ((input >> 16) & 0xffff) as i64;
	let part_three : i64 = ((input >> 32) & 0xffff) as i64;
	let part_four: i64 = ((input >> 48) & 0xffff) as i64;
	
	let p1 : i64 = *reversals.get(&part_one).unwrap();
	let output = (p1 << 48) 
			^ (*reversals.get(&part_two).unwrap() << 32)
			^ (*reversals.get(&part_three).unwrap() << 16)
			^ (*reversals.get(&part_four).unwrap());

	
	println!("{}", output);
}
