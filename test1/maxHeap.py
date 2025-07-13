class maxHeap:
    """class for Max Heap data structure
    """
    arr = []
    maxSize = 0
    heapSize = 0

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.arr = [None] * maxSize
        self.heapSize = 0

    def get_parent(self, i):
        """get parent index

        Args:
            i (int): index for which parent value to be needed

        Returns:
            int: return index for parent
        """
        return (i - 1) // 2

    def get_lchild(self, i):
        """get left child

        Args:
            i (int): index for which left child value to be needed

        Returns:
            int: return index for left child
        """
        return 2 * i + 1

    def get_rchild(self, i):
        """get right child

        Args:
            i (int): index for which right child value to be needed

        Returns:
            int: return index for right child
        """
        return 2 * i + 2

    def insert_key(self, data):
        """insert key to heap DS

        Args:
            data (int): data of the node to be inserted
        """

        if self.heapSize == self.maxSize:
            print("Overflow: could not insert key")
            return

        self.heapSize += 1
        i = self.heapSize - 1
        self.arr[i] = data

        # check max property and if violate, fix it
        # print(self.get_parent(i))
        while (i != 0 and self.arr[self.get_parent(i)] < self.arr[i]):
            temp = self.arr[self.get_parent(i)]
            self.arr[self.get_parent(i)] = self.arr[i]
            self.arr[i] = temp
            i = self.get_parent(i)

    def curr_size(self):
        """get current size of the heap data structure
        """

        return self.heapSize

    def get_max(self):
        """get max element, which is the root
        """
        return self.arr[0]

    def print_tree(self):
        """print complete tree
        """
        for i, data in enumerate(self.arr):
            print(data, end=" ")

    def increase_key(self, i, infinity):
        """move infinity to deleted values

        Args:
            i (int): index to be deleted
            infinity (float): store infinity value
        """
        self.arr[i] = infinity
        # move the infinity value to top
        while (i != 0 and self.arr[self.get_parent(i)] < self.arr[i]):
            temp = self.arr[self.get_parent(i)]
            self.arr[self.get_parent(i)] = self.arr[i]
            self.arr[i] = temp
            i = self.get_parent(i)

    def heapify(self, i):
        """max heapify the tree

        Args:
            i (int): starting value of the tree, which is 0
        """
        lchild = self.get_lchild(i)
        rchild = self.get_rchild(i)
        largest = i
        if (lchild < self.heapSize and self.arr[i] < self.arr[lchild]):
            largest = lchild

        if (rchild < self.heapSize and self.arr[i] < self.arr[rchild]):
            largest = rchild

        if largest != i:
            self.arr[largest], self.arr[i] = self.arr[i], self.arr[largest]
            self.heapify(largest)

    def remove_max(self):
        """remove root element
        """
        if self.heapSize <= 0:
            return None
        if self.heapSize == 1:
            self.heapSize -= 1
            return
        i = self.heapSize - 1
        self.arr[0] = self.arr[i]
        del self.arr[i]
        self.heapSize -= 1

        self.heapify(0)

    def delete_key(self, i):
        """delete key at index 2

        Args:
            i (int): index to be deleted
        """
        # move infinity to index i, and move it to top
        self.increase_key(i, float("inf"))
        # remove the max, and apple heapify operation
        self.remove_max()


if __name__ == "__main__":
    h = maxHeap(15)
    # insert 6 keys
    h.insert_key(3)
    h.insert_key(10)
    h.insert_key(12)
    h.insert_key(8)
    h.insert_key(2)
    h.insert_key(14)
    # Printing the current size
    # of the heap.
    print("The current size of the heap is "
          + str(h.curr_size()) + "\n")

    # Printing the root element which is
    # actually the maximum element.
    print("The current maximum element is " + str(h.get_max())
          + "\n")
    h.print_tree()
    print()
    # delete key
    # Deleting key at index 2.
    h.delete_key(2)
    h.print_tree()
   # Printing the size of the heap
    # after deletion.
    print("The current size of the heap is "
          + str(h.curr_size()) + "\n")

    # Inserting 2 new keys into the heap.
    h.insert_key(15)
    h.insert_key(5)
    print("The current size of the heap is "
          + str(h.curr_size()) + "\n")
    print("The current maximum element is " + str(h.get_max())
          + "\n")

    # print complete tree
    h.print_tree()
