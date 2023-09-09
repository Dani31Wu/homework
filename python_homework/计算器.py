# User: link
# Date: 2023/9/9
# File: 计算器
def calc(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print("算数运算符输入不合法，范围:(+-*/)")


flag = None  # 是否继续
while True:
    try:
        num1 = float(input("请输入第一个数："))
        num2 = float(input("请输入第二个数："))
        operator = input("请输入算术运算符(+-*/)：")
        result = calc(num1, num2, operator)
        if result:
            print(f"计算结果:{result}")
    except ZeroDivisionError:
        print('0不能作为除数')
    except ValueError:
        print('请输入有效的数')
    except Exception:
        print("程序异常")
    finally:
        flag = input("是否继续运算？（Y/N）")
        if flag.lower() == 'n':
            break
