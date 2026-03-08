from src.algorithm.dfs.tree_node import TreeNode


class IsSymmetric:

    """ 不能正确解题，有两个关键问题： 
    问题 1：中序遍历无法区分树的结构
    没有记录 None 占位符，不同结构的树会产生相同的遍历结果。反例：
         1              1
        / \            / \
       2   2          2   2
      /      \         \  /
     2        2        2  2
    左边是对称的，右边不对称，但中序遍历都是 [2, 2, 1, 2, 2]，代码会把两棵树都判为对称。

    问题 2：用值查找 root 位置不可靠

    当存在重复值时，result[i] == root.val 会找到第一个匹配，不一定是根的位置：
         1
        / \
        1   1
    中序遍历：[1, 1, 1]，代码在 i=0 就 break 了，认为 root 在索引 0，实际 root 在索引 """
    def is_symmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        result = []

        def in_order_traversal(node: TreeNode):
            nonlocal result
            if node.left is None and node.right is None:
                result.append(node.val)
                return

            if node.left:
                in_order_traversal(node.left)

            result.append(node.val)

            if node.right:
                in_order_traversal(node.right)

        in_order_traversal(root)
        """ 
        result_str = "".join(result)
        root_val = f"{root.val} "
        root_val_len = len(root_val)
        index = result_str.find(root_val)
        return result_str[:index] == result_str[index + root_val_len:]
        """
        i = 0
        n = len(result)
        while i < n:
            if result[i] == root.val:
                break
            if result[i] != result[n - 1 - i]:
                return False

            i += 1
        if i < n // 2 or n % 2 == 0:
            return False

        return True

    def is_symmetric_2(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def in_order_traversal(left_node: TreeNode, right_node: TreeNode) -> bool:
            if (left_node is None) != (right_node is None):
                return False
            elif left_node is None:
                return True

            if left_node.val != right_node.val:
                return False

            if (
                left_node.left is None
                and left_node.right is None
                and right_node.left is None
                and right_node.right is None
            ):
                return True

            if (left_node.left is not None) == (right_node.right is not None):
                if left_node.left:
                    if not in_order_traversal(left_node.left, right_node.right):
                        return False
            else:
                return False

            if (left_node.right is not None) == (right_node.left is not None):
                if left_node.right:
                    if not in_order_traversal(left_node.right, right_node.left):
                        return False
            else:
                return False

            return True

        return in_order_traversal(root.left, root.right)
    
    def is_symmetric_3(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def check(left_node: TreeNode, right_node: TreeNode) -> bool:
            if (not left_node) and (not right_node) :
                return True

            if (not left_node) or (not right_node) :
                return False

            if left_node.val != right_node.val:
                return False
            
            if not check(left_node.left, right_node.right):
                return False
            if not check(left_node.right, right_node.left):
                return False
            return True

        return check(root.left, root.right)
    
    def is_symmetri_ai(self, root: TreeNode) -> bool:
        if root is None:
            return True

        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val
                    and check(left.left, right.right)
                    and check(left.right, right.left))

        return check(root.left, root.right)
