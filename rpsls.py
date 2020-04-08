#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：吴温琪
日期：2020.4.8
"""

import random



# 0-石头
# 1-史波克
# 2-布
# 3-蜥蜴
# 4-剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	if name=="石头":
		num=0
	if name=="史波克":
		num=1
	if name=="布":
		num=2
	if name=="蜥蜴":
		num=3
	if name=="剪刀":
		num=4
	return num
	
	
def number_to_name(number):
	if number==0:
		name="石头"
	if number==1:
		name="史波克"
	if number==2:
		name="布"
	if number==3:
		name="蜥蜴"
	if number==4:
		name="剪刀"
	return name
	

def rpsls(player_choice):
	if player_choice in ["石头","剪刀","布","史波克","蜥蜴"]:
		print("-------------")
		print("您的选择为："+player_choice)
		num1=name_to_number(player_choice)
		num2=random.randrange(0,5)
		name2=number_to_name(num2)
		print("计算机的选择为：%s"%name2)
		if num1==0 and num2==3:
			print("您赢了")
		if num1==0 and num2==4:
			print("您赢了")
		if num1==1 and num2==0:
			print("您赢了")
		if num1==1 and num2==4:
			print("您赢了")
		if num1==2 and num2==1:
			print("您赢了")
		if num1==2 and num2==0:
			print("您赢了")
		if num1==3 and num2==1:
			print("您赢了")
		if num1==3 and num2==2:
			print("您赢了")
		if num1==4 and num2==2:
			print("您赢了")
		if num1==4 and num2==3:
			print("您赢了")
		if num1==num2:
			print("平局")
		if num2==0 and num1==3:
			print("机器赢了")
		if num2==0 and num1==4:
			print("机器赢了")
		if num2==1 and num1==0:
			print("机器赢了")
		if num2==1 and num1==4:
			print("机器赢了")
		if num2==2 and num1==1:
			print("机器赢了")
		if num2==2 and num1==0:
			print("机器赢了")
		if num2==3 and num1==1:
			print("机器赢了")
		if num2==3 and num1==2:
			print("机器赢了")
		if num2==4 and num1==2:
			print("机器赢了")
		if num2==4 and num1==3:
			print("机器赢了")
	else:
		print("Error: No Correct Name")
	
	


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
