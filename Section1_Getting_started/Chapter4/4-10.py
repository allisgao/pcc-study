#! python3

# get a list
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print 1st msg
print("The first three items in the list are: " )
print(foods[:3])

# print the 2nd msg
"""
##############想多了

## 找到中间3个元素。
##      方案1：人工查找法。不推荐。
##      方案2：通过算法分析。

### get the length of the list
f_len = len(foods)
### create an empty list
m_foods = []
##### 如果列表元素是奇数且大于等于3，就输出中间3个；
if f_len >= 3:
    middle_len = (f_len + 1) / 2
    m_foods = foods[middle_len - 1, middle_len + 2]
else:
    m_foods = foods
# 如果小于3个，就全输出。
"""
print("Three items from the middle of the list are:")
print(foods[1:4])

#TODO: print the 3rd msg
"""
##############想多了
m_foods2 = []
## 如果列表元素个数小于3个，全部输出；
if f_len <=3 :
    m_foods2 = foods
else:
    m_foods2 = foods[f_len- 3 : ]
print("The last three items in the list are: ")
print(m_foods2)
"""
print("The last three items in the list are: ")
print(foods[-3:])