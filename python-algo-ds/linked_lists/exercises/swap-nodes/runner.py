#!/bin/python3

import os
import sys


class Node:
    def __init__(self, index, depth):
        self.left = None
        self.right = None
        self.index = index
        self.depth = depth


def insert(indexes):
    num_of_nodes = len(indexes)
    root = Node(1, 1)
    cur = root

    queue = [cur]

    n = 0

    while n < num_of_nodes:
        cur = queue.pop(0)
        left_data = indexes[n][0]
        right_data = indexes[n][1]

        cur.left = None if left_data == -1 else Node(left_data, cur.depth + 1)
        cur.right = None if right_data == -1 else Node(right_data, cur.depth + 1)

        if cur.left is not None and cur.left.index != -1:
            queue.append(cur.left)
        if cur.right is not None and cur.right.index != -1:
            queue.append(cur.right)

        n = n + 1

    return root


def swap(root, depth, query):

    if root is None:
        return

    swap(root.left, depth + 1, query)
    swap(root.right, depth + 1, query)

    if depth >= query and depth % query == 0:
        temp = root.left
        root.left = root.right
        root.right = temp


def print_in_order(root):

    if root.left is not None:
        print_in_order(root.left)

    print(root.index)

    if root.right is not None:
        print_in_order(root.right)

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):

    root = insert(indexes)

    for query in queries:

        swap(root, 1, query)

    print_in_order(root)

    return 0


if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print(result)
