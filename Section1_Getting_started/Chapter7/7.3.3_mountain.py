#! python3

responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat's your name?\n")
    response = input("\nWhich mountain would you like to climb someday?\n")

    # 将反馈存储到字典中
    responses[name] = response

    # 看看是否还有人要参加调查
    repeat = input("Would you like to let another person respond? (yes/no)\n")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n-----  Poll Results -----")
for name, response in responses.items():
    print("%s would like to climb %s ." % (name.title(), response.title()))




