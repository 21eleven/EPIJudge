object count_bits{
	def countBits(integer:Int) : Int = {
		var c : Int = 0
		var x : Int = integer

		while (x > 0) {
			c += 1
			x = x & (x -1)
		}
		return c
	}

	def main(args: Array[String]) {
		println(countBits(args(0).toInt))
	}
}

