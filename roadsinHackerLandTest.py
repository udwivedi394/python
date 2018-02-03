n, m = map(int, raw_input().split())
e = []
for i in range(m):
    u, v, c = map(int, raw_input().split())
    e.append((c, u - 1, v - 1))

parent = [i for i in range(n)]


def find_set(v):
    global parent
    if parent[v] != v:
        parent[v] = find_set(parent[v])
    return parent[v]

print "OrgEdge:",e
print "ParentOrg:",parent

e.sort()
print "AfterSort:",e

g = [[] for i in range(n)]

for (c, u, v) in e:
    a, b = find_set(u), find_set(v)
    if a != b:
        parent[a] = b
        g[u].append((v, c))
        g[v].append((u, c))

ans = [0] * (m * 2)


def dfs(v, p=-1):
    global ans
    cur_size = 1
    for (to, c) in g[v]:
        if to != p:
            sz = dfs(to, v)
            ans[c] += sz * (n - sz)
            cur_size += sz
    return cur_size

print "ans:",ans
print "G:",g
dfs(0)
print "Afterans:",ans

for i in range(len(ans) - 1):
    ans[i + 1] += ans[i] / 2
    ans[i] %= 2

print "Laterans:",ans

flag = False
real_ans = []
for i in range(len(ans) - 1, -1, -1):
    if flag or ans[i] > 0:
        flag = True
        real_ans.append(ans[i])

print "Realans:",real_ans
print "".join(map(str, real_ans))
