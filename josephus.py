# coding:utf-8
'''
数字从1到n
从1号报数，到k时，dead，下一个从1开始报数

n = 5, k = 2
第一轮应是2,4
第二轮应是1,5
最终剩下3

'''

def josephus(n, k):
    if k == 1:
        print('survive:', n)
        return
    p = 0
    total = range(1, n + 1)
    while True:
        if len(total) == 1:
            break
        p = (p + (k - 1)) % len(total)
        print 'kill:', total[p]
        del total[p]
    print 'survive:', total[0]

if __name__ == '__main__':
    josephus(5, 2)
