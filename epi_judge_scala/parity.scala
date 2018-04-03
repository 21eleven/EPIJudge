object parity {
	def parity(integer:Int) : Int = {
		var parity : Int = 0
		var x : Int = integer

		while (x > 0) {
			parity ^= 1
			x = x & (x -1)
		}
		return parity
	}

	def main(args: Array[String]) {
		println(parity(args(0).toInt))
	}
}

