package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTestHandler;

public class PrimitiveDivide {
  @EpiTest(testfile = "primitive_divide.tsv")
  public static int divide(int x, int y) {
    // Implement this placeholder.
    short power = 32;
    int result = 0;
    while (x >= y) {
    	while (1 << power > x) {
	  power -= 1;
	}
	result += 1 << power;
	x -=  y << power;
    }
    return result;
  }

  public static void main(String[] args) {
    GenericTestHandler.executeTestsByAnnotation(
        new Object() {}.getClass().getEnclosingClass(), args);
  }
}
