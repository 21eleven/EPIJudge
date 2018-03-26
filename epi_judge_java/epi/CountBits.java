package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTestHandler;

public class CountBits {
  @EpiTest(testfile = "count_bits.tsv")

  public static short countBits(int x) {
    // Implement this placeholder.
    short count = 0;
    while (x > 0) {
      count += 1;
      x = x & x - 1;
    }
    return count;
  }

  public static void main(String[] args) {
    GenericTestHandler.executeTestsByAnnotation(
        new Object() {}.getClass().getEnclosingClass(), args);
  }
}
