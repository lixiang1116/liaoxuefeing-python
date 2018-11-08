# -*- coding:utf-8 -*-

#1 排序算法
print sorted([36,5,-12,9,-21])

#2 sorted 高阶函数

print sorted([36,5,-12,9,-21],key=abs)

#3 练习题 假设我们用一组tuple表示学生名字和成绩：L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]，请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    name=t[0]
    return name
def by_score(t):
    score=t[1]
    return score
print sorted(L,key=by_name)
print sorted(L,key=by_score,reverse=True)



