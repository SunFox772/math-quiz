import random

print("欢迎使用随机数学口算题生成器！")

while True:
    try:
        num = int(input("请输入题目数量: "))
        if num <= 0:
            print("请输入一个正整数！")
            continue
        break
    except ValueError:
        print("请输入一个有效的整数！")


for i in range(num):
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a + b
    elif operator == '-':
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a - b
    elif operator == '*':
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        answer = a * b
    else:
        b = random.randint(1, 20)
        answer = random.randint(1, 20)
        a = b * answer      # 为确保整除，除法采用 被除数 = 商 * 除数 的方式倒推


    while True:
        user_answer = input(f"题目 {i+1}: {a} {operator} {b} = ")

        try:
            user_value = int(user_answer)       # 得到纯净的答案
            break
        except ValueError:
            print("请输入一个整数！")


    if user_value == answer:            # 判断正误
        print("回答正确！")
    else:
        print(f"回答错误，正确答案是: {answer}")
