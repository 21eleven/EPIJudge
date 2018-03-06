package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class CollatzChecker {
  @EpiTest(testfile = "collatz_checker.tsv")

  public static boolean testCollatzConjecture(int n) {
    // Implement this placeholder.
    return false;
  }

  public static void main(String[] args) {
    // The timeout is set to 15 seconds for each test case.
    // If your program ends with TIMEOUT error, and you want to try longer time
    // limit, you can extend the limit by changing the following line.
    long timeoutSeconds = 15;

    System.exit(
        GenericTest
            .runFromAnnotations(args, timeoutSeconds,
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
