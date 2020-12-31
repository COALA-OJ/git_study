# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

n, m = map(int, input().split())


List = [0 for _ in range(n)]

newlist = []
for i in range(n):
    List[i] = list(map(int, input().split()))
    for j in range(m):
        if List[i][j] == 2:
            newlist.append([i, j])

print(newlist)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
