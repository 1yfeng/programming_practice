from __future__ import annotations
from typing import Optional
from collections import deque

class BiTreeNode:
    def __init__(self, value: int | str | None, 
                 left: Optional[BiTreeNode] = None,
                 right: Optional[BiTreeNode] = None,):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: Optional[BiTreeNode] = None):
        self.root = root

    
    @classmethod
    def from_traversal_sequence(cls, trav_seq: str | None = None):
        if not str:
            return cls()
        
        cur_index = 0
        def pre_order_traversal() -> BiTreeNode:
            nonlocal cur_index
            nonlocal trav_seq
            
            if trav_seq and cur_index < len(trav_seq) and trav_seq[cur_index] != "#":
                node = BiTreeNode(trav_seq[cur_index])
                cur_index += 1 
                node.left = pre_order_traversal()
                node.right = pre_order_traversal()
                return node
            else:
                cur_index += 1 
                return None
        return cls(pre_order_traversal())

    def print_tree(self) -> None:
        """按层打印二叉树，直观显示树形结构"""
        if self.root is None:
            print("<空树>")
            return

        lines = []
        self._build_lines(self.root, lines)
        for line in lines:
            print(line)

    def _build_lines(self, node: Optional[BiTreeNode], lines: list) -> tuple:
        """递归构建每个节点的显示行，返回 (行列表, 根节点在第一行的起始位置, 宽度)"""
        if node is None:
            return [], 0, 0

        val_str = str(node.value)
        val_len = len(val_str)

        # 叶子节点
        if node.left is None and node.right is None:
            lines.append(val_str)
            return [val_str], 0, val_len

        left_lines, left_pos, left_width = self._build_lines(node.left, [])
        right_lines, right_pos, right_width = self._build_lines(node.right, [])

        # 只有左子树
        if node.right is None:
            first_line = ' ' * (left_pos + 1) + '_' * (left_width - left_pos - 1) + val_str
            second_line = ' ' * left_pos + '/' + ' ' * (left_width - left_pos - 1 + val_len)
            shifted = [line + ' ' * val_len for line in left_lines]
            result = [first_line, second_line] + shifted
            lines.extend(result)
            return result, left_width, left_width + val_len

        # 只有右子树
        if node.left is None:
            first_line = val_str + '_' * right_pos + ' ' * (right_width - right_pos)
            second_line = ' ' * (val_len + right_pos) + '\\' + ' ' * (right_width - right_pos - 1)
            shifted = [' ' * val_len + line for line in right_lines]
            result = [first_line, second_line] + shifted
            lines.extend(result)
            return result, 0, val_len + right_width

        # 左右子树都有
        gap = 1
        first_line = (' ' * (left_pos + 1) + '_' * (left_width - left_pos - 1) +
                       val_str +
                       '_' * right_pos + ' ' * (right_width - right_pos))
        second_line = (' ' * left_pos + '/' +
                        ' ' * (left_width - left_pos - 1 + val_len + right_pos) +
                        '\\' + ' ' * (right_width - right_pos - 1))
        
        # 合并左右子行，对齐
        max_lines = max(len(left_lines), len(right_lines))
        left_lines += [' ' * left_width] * (max_lines - len(left_lines))
        right_lines += [' ' * right_width] * (max_lines - len(right_lines))
        merged = [l + ' ' * (gap + val_len) + r for l, r in zip(left_lines, right_lines)]

        result = [first_line, second_line] + merged
        lines.extend(result)
        return result, left_width, left_width + val_len + gap + right_width

    def level_order_str(self) -> str:
        """层序遍历输出，方便快速查看"""
        if self.root is None:
            return "[]"
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.value))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        # 去掉末尾多余的 null
        while result and result[-1] == "null":
            result.pop()
        return "[" + ", ".join(result) + "]"


    def visit(self, node: Optional[BiTreeNode]):
        print(getattr(node, 'value', "None"))

    def pre_oder_traversal():
        ...
    def pre_order_iter(self, node: Optional[BiTreeNode]= None):
        if node is None:
            node = self.root
        
        stack = []
        self.visit(node)
        stack.append(node)
        last_oper_pop = False

        while stack:
            node = stack[-1]
            node = node.left
            if node and not last_oper_pop:
                self.visit(node)
                stack.append(node)
                last_oper_pop = False
            else:
                node = stack.pop()
                node = node.right
                if node:
                    self.visit(node)
                    stack.append(node)
                    last_oper_pop = False
                else:
                    last_oper_pop = True

    def pre_order_iter_opt(self, node: Optional[BiTreeNode]= None):
        if node is None:
            node = self.root
        
        stack = []
        stack.append(node)
        while stack:
            node = stack.pop()
            self.visit(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def in_order_iter(self, node: Optional[BiTreeNode]= None):
        if node is None:
            node = self.root
        
        stack = []
        stack.append(node)
        last_oper_pop = False

        while stack:
            node = stack[-1]
            node = node.left
            if node and not last_oper_pop:
                stack.append(node)
                last_oper_pop = False
            else:
                node = stack.pop()
                self.visit(node)
                node = node.right
                if node:
                    stack.append(node)
                    last_oper_pop = False
                else:
                    last_oper_pop = True

    def in_oder_traversal():
        ...
    def post_oder_traversal():
        ...
    
    def _oder_traversal():
        return

