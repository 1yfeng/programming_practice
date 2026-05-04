"""
LeetCode 69. x 的平方根

给你一个非负整数 x，计算并返回 x 的算术平方根（整数部分）。
不允许使用内置指数函数和算符。
"""


# 推荐解：二分搜索  O(log x)
def my_sqrt_binary_search(x: int) -> int:
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == x:
            return mid
        elif sq < x:
            left = mid + 1
        else:
            right = mid - 1
    # 循环结束时 right < left，right 是满足 right*right <= x 的最大整数
    return right


# 经典解：牛顿迭代法  O(log x)，收敛极快
def my_sqrt_newton(x: int) -> int:
    if x < 2:
        return x
    r = x
    while r * r > x:
        r = (r + x // r) // 2
    return r
