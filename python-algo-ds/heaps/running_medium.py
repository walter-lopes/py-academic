#!/bin/python3

import os
import sys
import heapq
#
# Complete the runningMedian function below.
#

def calc_median(max_heap, min_heap):
    if len(max_heap) == 0:
        return 0
    elif len(max_heap) == len(min_heap):
        return (max_heap[0] + min_heap[0]) / 2.0
    return max_heap[0]

def add_number(number, max_heap, min_heap):

    if len(max_heap) == 0:
        heapq.heappush(max_heap, number)

    elif len(max_heap) == len(min_heap):
        if number < min_heap[0]:
            heapq.heappush(max_heap, number)
        else:
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap):
        if number > max_heap[0]:
            heapq.heappush(min_heap, number)
        else:
            heapq.heappush(max_heap, number)
            heapq.heappush(min_heap, heapq.heappop(max_heap))

def runningMedian(a):
    result = []
    max_heap = []
    min_heap = []
    for x in range(len(a)):
        add_number(a[x], max_heap, min_heap)
        result.append(calc_median(max_heap, min_heap))

    return result

if __name__ == '__main__':
    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

