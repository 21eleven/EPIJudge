use std::env;

fn add(a:u64, b:u64) -> u64 {
    let mut result = 0u64;
    let mut carry = 0u64;
    let mut idx = 0u64;

    loop {
        let a_bit = a >> idx & 1;
        let b_bit = b >> idx & 1;
	/*
	println!("{}", idx);
	println!("a {}, b {}, carry {}", a_bit, b_bit, carry);
	*/
        if a_bit & b_bit == 1 {
            if carry == 1 {
                result = result ^ 1 << idx;
            } else {
                carry = 1;
            }
        }
        if a_bit ^ b_bit == 1 {
            if carry == 1 {
                carry = 1;
            } else {
                result = result ^ 1 << idx;
            }
        }
        if a_bit | b_bit == 0 {
            if carry == 1 {
                result = result ^ 1 << idx;
                carry = 0;
            }
        }


        if (a >> idx) | (b >> idx) == 0 {
            break
        }

	idx += 1;
    }
    result
}

fn multiply(a:u64,b:u64) -> u64 {
    let mut idx = 0u64;
    let mut result = 0u64;
    //let mut shift = 0u64;
    loop {
	if a >> idx & 1 == 1 {
	    let shift = b << idx;
	    result = add(result, shift);
	}
	if a >> idx == 0 { break }
	idx += 1;
    }
    result
}    

fn main() {
    let args: Vec<String> = env::args().collect();
    let a = args[1].parse::<u64>().unwrap();
    let b = args[2].parse::<u64>().unwrap();

    let output = multiply(a,b);

    //println!("{} {} -> {}", a,b,output);
    //println!("{:b} {:b} -> {:b}", a,b,output);
    println!("{}", output)
}
