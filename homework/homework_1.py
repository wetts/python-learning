# -*- coding: utf-8 -*-
'''
一个年轻人毕业了，想要买个房子，但是得攒几年的钱才够首付，请你帮忙算一下他要多久才能买得起房
1）令房子的价格为 total_cost
2）令首付的比例为 portion_down_payment，在这里我们赋值为0.25
3）令目前年轻人手头上的存款为current_savings，在这里我们赋值为0
4）假设年轻人拿手头上的存款来投资，年利率为r，在这里我们赋值为0.04（月利率为r/12）
5）假设年轻人的一年的工资为annual_salary（月工资为annual_salary/12）
6）假设年轻人每年会将工资的一部分存起来，比例为portion_saved
7）每个月底，存款的投资利率都会到账，工资也会到账
写一个程序来计算需要多少个月年轻人才能付得起首付
程序需要用户输入三个数值，annual_salary，portion_saved，total_cost
程序输出月份个数

要求用函数形式 (要有定义函数，调用函数的过程)
'''


#################在下方写入你的代码##########################
import math


def cal(annual_salary, portion_saved, total_cost, current_savings=0, portion_down_payment=0.25, annual_interest_rate=0.04):
    month_saved = annual_salary * portion_saved / 12
    month_interest_rate = annual_interest_rate / 12
    down_payment = total_cost * portion_down_payment

    x = math.log(down_payment / month_saved * month_interest_rate + 1, 1 + month_interest_rate)

    return math.ceil(x)


print(cal(120000, 0.1, 1000000))
print(cal(80000, 0.15, 500000))
##########################################################


'''
示例1
annual salary: 120000
percent of salary to save: 0.10
cost of house: 1000000
number of month: 183

示例2
annual salary: 80000
percent of salary to save: 0.15
cost of house: 500000
number of month: 105
'''


'''
在上面一题我们没有考虑到年轻人会涨工资的情况，因此情况可能比预计的要乐观
1）假设年轻人每次涨工资的幅度为semi_annual_raise
2）年轻人每6个月涨一次工资
其他的情况保持不变
现在再计算一下年轻人要多久才能付得起首付吧。
要求用函数形式 (要有定义函数，调用函数的过程)
'''
#################在下方写入你的代码##########################


def cal2(annual_salary, portion_saved, total_cost, semi_annual_raise, current_savings=0, portion_down_payment=0.25, annual_interest_rate=0.04):
    month_salary = annual_salary / 12
    month_saved = month_salary * portion_saved
    month_interest_rate = annual_interest_rate / 12
    down_payment = total_cost * portion_down_payment

    month = 0
    total_saved = 0
    while True:
        if total_saved >= down_payment:
            break

        month += 1

        if month % 6 == 0:
            month_salary *= 1 + semi_annual_raise
            month_saved = month_salary * portion_saved

        total_saved *= 1 + month_interest_rate
        total_saved += month_saved

    return month


print(cal2(120000, 0.05, 500000, 0.03))
print(cal2(80000, 0.1, 800000, 0.03))
print(cal2(75000, 0.05, 1500000, 0.05))
##########################################################


'''
示例1
annual salary: 120000
percent of salary to save: 0.05
cost of house: 500000
semi-annual raise: 0.03
number of month: 142

示例2
annual salary: 80000
percent of salary to save: 0.1
cost of house: 800000
semi-annual raise: 0.03
number of month: 158

示例3
annual salary: 75000
percent of salary to save: 0.05
cost of house: 1500000
semi-annual raise: 0.05
number of month: 260
'''
################作业三#######################
'''
输入两个字符串，从第一字符串中删除第二个字符串中所有的字符，然后再反向输出。
- 输入描述：每个测试输入包含2个字符串
- 输出描述：反向输出删除后的字符串
'''
#################在下方写入你的代码##########################


def function(str1, str2):
    return "".join([s for s in str1 if s not in str2][::-1])


# s1 = input('s1:')
# s2 = input('s2:')
# s = function(s1, s2)
s = function('They are students.', 'aeiou')
print(s)
##########################################################
'''
例如，输入”They are students.”和”aeiou”,则删除之后的第一个字符串变成”Thy r stdnts.”
然后反向输出的最终结果为：".stndts r yhT"
'''
