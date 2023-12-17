#!/usr/bin/python3
seq = ["{:02d}".format(i) for i in range(1, 90) if i % 10 > i // 10]
print(", ".join(seq))
