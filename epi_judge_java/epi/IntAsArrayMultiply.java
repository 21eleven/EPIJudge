package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.List;

public class IntAsArrayMultiply {
  @EpiTest(testfile = "int_as_array_multiply.tsv")
  public static List<Integer> multiply(List<Integer> num1, List<Integer> num2) {
    // Implement this placeholder.
    return null;
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
