def fibonacci_bottom_up(n, ans=None):
    if n in (0, 1):
        return 1
    ans = [0] * (n + 1)
    ans[0] = 1
    ans[1] = 1
    for i in range(2, len(ans)):
        ans[i] = ans[i - 1] + ans[i - 2]
    return ans[n]


def fibonacci_classic(n):
    if n in (0, 1):
        return 1
    return fibonacci_classic(n - 1) + fibonacci_classic(n - 2)
