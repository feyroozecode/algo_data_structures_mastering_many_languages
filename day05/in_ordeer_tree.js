/**
 * Implementation Details
 * The function uses an iterative approach with a stack to simulate the recursive inorder traversal.
 * It initializes an empty result array to store the values.
 * A while loop is used to traverse the tree until all nodes are visited.
 * The algorithm pushes nodes onto the stack while moving to the leftmost child.
 * When a node is popped from the stack, its value is added to the result array.
 * The algorithm then moves to the right child of the popped node. Complexity .
 * Time Complexity: O(N) where N is the number of nodes in the tree.
 * Space Complexity: O(H) where H is the height of the tree, representing the maximum size of the stack.
 */
import TreeNode from './treenode.mjs'

function in_order_traversal(root) {
  const result = [];
  const stack = [];

  let current = root;

  while (current || stack.length > 0) {
    while (current) {
      stack.push(current);
      current = current.left;
    }

    current = stack.pop();
    result.push(current.value);
    current = current.right;
  }

  return result;
}

// Example Usage:
// Construct a sample binary tree
const root = new TreeNode(1);
root.left = new TreeNode(2);
root.right = new TreeNode(3);
root.left.left = new TreeNode(4);
root.left.right = new TreeNode(5);

// Perform inorder traversal starting from the root
const result = in_order_traversal(root);
console.log(result); // Output: [4, 2, 5, 1, 3]
