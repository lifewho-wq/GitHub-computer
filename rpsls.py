#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020.4.8
"""

import random



# 0-ʯͷ
# 1-ʷ����
# 2-��
# 3-����
# 4-����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	if name=="ʯͷ":
		num=0
	if name=="ʷ����":
		num=1
	if name=="��":
		num=2
	if name=="����":
		num=3
	if name=="����":
		num=4
	return num
	
	
def number_to_name(number):
	if number==0:
		name="ʯͷ"
	if number==1:
		name="ʷ����"
	if number==2:
		name="��"
	if number==3:
		name="����"
	if number==4:
		name="����"
	return name
	

def rpsls(player_choice):
	if player_choice in ["ʯͷ","����","��","ʷ����","����"]:
		print("-------------")
		print("����ѡ��Ϊ��"+player_choice)
		num1=name_to_number(player_choice)
		num2=random.randrange(0,5)
		name2=number_to_name(num2)
		print("�������ѡ��Ϊ��%s"%name2)
		if num1==0 and num2==3:
			print("��Ӯ��")
		if num1==0 and num2==4:
			print("��Ӯ��")
		if num1==1 and num2==0:
			print("��Ӯ��")
		if num1==1 and num2==4:
			print("��Ӯ��")
		if num1==2 and num2==1:
			print("��Ӯ��")
		if num1==2 and num2==0:
			print("��Ӯ��")
		if num1==3 and num2==1:
			print("��Ӯ��")
		if num1==3 and num2==2:
			print("��Ӯ��")
		if num1==4 and num2==2:
			print("��Ӯ��")
		if num1==4 and num2==3:
			print("��Ӯ��")
		if num1==num2:
			print("ƽ��")
		if num2==0 and num1==3:
			print("����Ӯ��")
		if num2==0 and num1==4:
			print("����Ӯ��")
		if num2==1 and num1==0:
			print("����Ӯ��")
		if num2==1 and num1==4:
			print("����Ӯ��")
		if num2==2 and num1==1:
			print("����Ӯ��")
		if num2==2 and num1==0:
			print("����Ӯ��")
		if num2==3 and num1==1:
			print("����Ӯ��")
		if num2==3 and num1==2:
			print("����Ӯ��")
		if num2==4 and num1==2:
			print("����Ӯ��")
		if num2==4 and num1==3:
			print("����Ӯ��")
	else:
		print("Error: No Correct Name")
	
	


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
