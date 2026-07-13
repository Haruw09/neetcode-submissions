class Node:

    def __init__(self, key: int | None = None, value: int | None = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_end(self, node: Node) -> Node:
        prev_node = self.right.prev

        node.prev = prev_node
        node.next = self.right

        self.right.prev = node
        prev_node.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert_at_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
        else:
            node = Node(key, value)
        
        self._insert_at_end(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            node = self.left.next
            key = node.key
            self._remove(node)
            del self.cache[key]

        

        
