#! python3
lang_dic = {
    'python': 'python language',
    'c': 'c language',
    'ruby': 'ruby language',
    'java': 'java language',
    'c#': 'c# language'
    }
# print language and its explain
for k,v in lang_dic.items():
    #print("%s  :  %s\n" % (k,v))
    print("Key: " + k.title() + " \nValue: " + v.title() + '\n')