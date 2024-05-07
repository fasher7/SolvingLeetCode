class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        node = queue.pop(0)
        if nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root, height):
            if not root:
                return height-1
            lheight = depth(root.left, height+1)
            rheight = depth(root.right, height+1)
            return max(lheight, rheight)

        if not root:
            return 0
        else:
            return depth(root, 1)

root = [3,9,20,None,None,15,7]
root = build_tree(root)
md = Solution()
print(md.maxDepth(root))