#! python3

# 统计词频

import collections, re

filename = "Hamlet.txt"



def count_word(file):
    result = {}
    with open(file, encoding='utf8') as file_obj:
        all_the_text = file_obj.read()
        # 大写转小写
        all_the_text = all_the_text.lower()
        # 正则表达式替换特殊字符
        all_the_text = re.sub("\"|,|\.", "", all_the_text)

        for word in all_the_text.split():
            if word not in result:
                result[word] = 0
            result[word] += 1
        return result
        #print(str(result))


### 词频倒序
def sort_by_count(d):
    # 字典排序
    d = collections.OrderedDict(sorted(d.items(), key=lambda t: -t[1]))
    return d

dword = count_word(filename)
dword = sort_by_count(dword)

for k, v in dword.items():
    print(k + " : " + str(v))
