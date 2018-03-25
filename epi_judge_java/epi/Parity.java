package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTestHandler;

public class Parity {
  @EpiTest(testfile = "parity.tsv")
  public static short parity(long x) {
    // Implement this placeholder.
    short parity = 0;

    while ( x != 0 ) {
	  parity ^= 1;
	  x = x & x - 1;
    }
    return parity;
  }

  public static void main(String[] args) {
    GenericTestHandler.executeTestsByAnnotation(
        new Object() {}.getClass().getEnclosingClass(), args);
  }
}
