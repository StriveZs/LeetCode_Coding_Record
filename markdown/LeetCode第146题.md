---
title: LeetCode No.146

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第146题—LRU缓存机制
回家休息几天，搬宿舍心累。再回实验室就开始好好科研了！！！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

```
示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put
```

## LRU缓存机制介绍
LRU：最近最少使用缓存机制

其设计的原则依据：如果一个数据在最近一段时间没有被访问到，那么在将来它被访问的可能性也很小。也就是说，当限定的空间已存满数据时，应当把最久没有被访问到的数据淘汰。
假定系统为某进程分配了3个物理块，进程运行时的页面走向为 7 0 1 2 0 3 0 4，开始时3个物理块均为空，那么LRU算法是如下工作的：

![figure.1](https://img-blog.csdnimg.cn/20191102105842382.png)

## 代码
### 自己写的
效率和内存差了点，但是自己纯手工写的。QAQ  
核心思想就是通过使用双向链表和字典来存储内容。  
```
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
```