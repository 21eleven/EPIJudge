package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.List;

public class TreeWithParentInorder {
  @EpiTest(testfile = "tree_with_parent_inorder.tsv")

  public static List<Integer> inorderTraversal(BinaryTree<Integer> tree) {
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
