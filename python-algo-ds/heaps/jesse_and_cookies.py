class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

        # for checking if the queue is empty

    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

        # for popping an element based on Priority

    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

    def peek(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            return item
        except IndexError:
            print()
            exit()

import heapq

def cookies(k, A):

    counter = 0
    heapq.heapify(A)

    while len(A) > 0 and A[0] <= k:
        if len(A) == 0:
            break

        first = heapq.heappop(A)

        if len(A) == 0:
            break


        second = heapq.heappop(A)

        heapq.heappush(A, first + 2 * second)
        counter = counter + 1

    if len(A) == 0 or A[0] < k:
        print(-1)
    else:
        print(counter)

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)