package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.List;

public class FirstMissingPositiveEntry {
  @EpiTest(testfile = "first_missing_positive_entry.tsv")

  public static int findFirstMissingPositive(List<Integer> A) {
    // Implement this placeholder.
    return 0;
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
