"""A.k.a. write a parser.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'Node({self.val}, {self.left}, {self.right})'


def deserialize(json):
    def read_string(s):
        val = s.split('"')[3]
        return val, s.index(val) + len(val) + 1

    def read_node(s, begin=0):
        # assert s[pos] == '{'
        node = Node("")
        pos = begin
        while pos < len(s):
            c = s[pos]
            if c == '}':
                print(node)
                return node, pos - begin
            if s[pos:pos + 5] == '"val"':
                node.val, size = read_string(s[pos:])
                pos += size
            if s[pos:pos + 6] == '"left"':
                node.left, size = read_node(s[pos + 7:])
                pos += size
            if s[pos:pos + 6] == '"right"':
                node.right, size = read_node(s[pos:])
                pos += size
            else:
                pos += 1

    node, _ = read_node(json)
    return node


def serialize(node):
    if node.left and node.right:
        return f'{{"val": "{node.val}", "left": {serialize(node.left)}, "right": {serialize(node.right)}}}'
    if node.left:
        return f'{{"val": "{node.val}", "left": {serialize(node.left)}}}'
    if node.right:
        return f'{{"val": "{node.val}", "right": {serialize(node.right)}}}'
    else:
        return f'{{"val": "{node.val}"}}'


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
