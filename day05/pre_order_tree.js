class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Recursive Preorder Traversal
function preorderTraversalRecursive(root) {
  const result = [];

  function traverse(node) {
    if (node !== null) {
      // Process the current node (e.g., push its value to the result array)
      result.push(node.value);

      // Traverse the left subtree
      traverse(node.left);

      // Traverse the right subtree
      traverse(node.right);
    }
  }

  traverse(root);
  return result;
}

// Iterative Preorder Traversal
function preorderTraversalIterative(root) {
  const result = [];
  const stack = [];

  if (root !== null) {
    stack.push(root);

    while (stack.length > 0) {
      const node = stack.pop();

      // Process the current node (e.g., push its value to the result array)
      result.push(node.value);

      // Push the right child first (since it will be processed after the left child)
      if (node.right !== null) {
        stack.push(node.right);
      }

      // Push the left child
      if (node.left !== null) {
        stack.push(node.left);
      }
    }
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

// Perform iterative preorder traversal starting from the root
const resultIterative = preorderTraversalIterative(root);
console.log("Iterative:", resultIterative); // Output: [1, 2, 4, 5, 3]
