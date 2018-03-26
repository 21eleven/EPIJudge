package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTestHandler;

public class PrimitiveMultiply {
  @EpiTest(testfile = "primitive_multiply.tsv")
  public static long multiply(long x, long y) {
    // Implement this placeholder.
    long product = 0;
    while (x > 0 ) {
    	if (( x & 1)==1) {
		product = add(product,y);
	}
	y <<= 1;
	x >>= 1;
    }
    return product;
  }

  public static long add(long a, long b) {
    short carry = 0;
    long sum = 0;
    long place = 1;
    while ((a > 0) || (b > 0) || (carry >0)) {
	    if (((a & 1)==1) && ((b & 1)==1)) {
	      if (carry == 0) {
		carry = 1;
	      } else {
	        sum ^= place;
	      }
	    } else if (((a & 1)==1) || ((b & 1)==1)) {
	      if (carry == 0) {
		sum ^= place;
	      } 
	    } else {
	      if (carry == 1) {
		sum ^= place;
		carry = 0;
	      }
	    }
	    a >>= 1;
	    b >>= 1;
	    place <<= 1;
    }
    return sum;
  }

  public static void main(String[] args) {
    GenericTestHandler.executeTestsByAnnotation(
        new Object() {}.getClass().getEnclosingClass(), args);
  }
}
