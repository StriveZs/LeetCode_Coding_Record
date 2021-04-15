# 滑动窗口
```
lo, hi = 0, 0
while hi < n:
    window += grumpy[hi] * customers[hi]        # 右值进入窗口
    while hi - lo + 1 > X:                      # 维护大小为X的窗口
        window -= grumpy[lo] * customers[lo]    # 左值退出窗口
        lo += 1                                 # 左指针前进1
    <do...>                                     # 任务1
    hi += 1                                     # 右指针前进1
```