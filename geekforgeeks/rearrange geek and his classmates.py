class Solution:
    def prank(self,a,n):
        for i in range(n):
            b = a[i]
            c = a[b]
            a[i] = c

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ob.prank(a,n)
        for i in a:
            print(i,end=" ")
        print()
