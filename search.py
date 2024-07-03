from collections import deque

# 图的数据可以使用散列表存储，即数组和链表的结合
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# 广度优先搜索
def search(name):
    # 创建一个存储朋友的双端队列，每次从左边弹出，右边添加
    search_queue = deque()
    search_queue += graph[name]
    # 创建一个空列表，用于存储检查过的朋友
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller')
                return True
            else:
                search_queue += graph[person]
                # 记得将朋友添加进空列表中
                searched.append(person)

    return False


# 判断实参对象是否为商人
def person_is_seller(person):
    # 检查方法为判断名字最后是否有一个'm'
    if person[-1] == 'm':
        return True
    else:
        return False


search('you')
