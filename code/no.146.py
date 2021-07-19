class LRUCache(object):
    """
    LRU 最近最少使用缓存机制：
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    对上面例子分析:
        1. LRUCache 2 表示：创建一个容量为2的LRU缓存
        2. put表示执行put操作，把1放到LRU中，并设置它的使用次数为1 其他所有数值的使用次数-1
        3. put 2，2表示：把2放到LRU中，并设置它的使用次数为1 其他所有数值的使用次数-1
        4. get 1表示使用一次LRU中的1，并将它的使用次数+1  其他所有数值的使用次数-1
        5. put 3，3表示：把3放入到LRU中，因为LRU已经满了，因此需要将使用次数最小的那个值(2)置换出来，把3放进入 其他所有数值的使用次数-1

    使用字典来存储key-value
    使用list作为双端链表来存储使用次数
    """
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.length = capacity
        self.lru_cache = [] # 双端链表，头部表示最新使用的节点，尾部是最久没使用的节点
        self.key_value = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_value.keys():
            return -1
        else:
            # 如果能够获取，将访问的node放置于链表最前头
            self.lru_cache.remove(key)
            self.lru_cache.insert(0,key) # 置于链表头部
            return self.key_value[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_value.keys():
            self.key_value[key] = value  # 更新
            # 如果能够获取，将访问的node放置于链表最前头
            self.lru_cache.remove(key)
            self.lru_cache.insert(0, key)  # 置于链表头部
        else:
            if len(self.key_value) < self.length:
                self.lru_cache.insert(0, key)  # 置于链表头部
                self.key_value[key] = value
            else:
                # 链表末尾元素出链表
                rm_key = self.lru_cache[-1]
                self.lru_cache.pop()
                self.key_value.pop(rm_key)

                # 添加新的元素
                self.lru_cache.insert(0, key)  # 置于链表头部
                self.key_value[key] = value

if __name__ == '__main__':
    t1 = ["LRUCache","get","put","get","put","put","get","get"]

    t2 = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    t = None
    for i in range(len(t1)):
        if t1[i] == 'LRUCache':
            t = LRUCache(t2[i][0])
            print('None')
        elif t1[i] == 'put':
            print(t.put(t2[i][0], t2[i][1]))
        elif t1[i] == 'get':
            print(t.get(t2[i][0]))