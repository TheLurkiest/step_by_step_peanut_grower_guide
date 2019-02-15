print("testing the list out now2...")

p_list = [-9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, 9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, 9999.1, -9999, -9999, -9999, -9999, -9999, -9999, 9999, -9999, -9999, -9999, -9999, -9999, -9999, 9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, 9999.1, 9999.1, 9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999.1, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, -9999, True, False]

#print("the list said this for value 1: " + str(p_list[0]))
#print("the list said this for value 2: " + str(p_list[1]))

print("the list said this for the first two values: " + str(p_list[:2]))
print("the list said this for the last three values: " + str(p_list[-3:]))

#s1 = ("1)Choose which variety of peanuts to plant in your plot of land-- Choose from one of the following Cultivar Groups:   1a) Spanish Group (commonly grown in South Africa): Spanish peanuts are most often used to make peanut butter and candy because of their higher oil content. The Spanish variety produces small nuts with a brownish-red skin. Spanish peanuts need about 90 to 130 days for maturity.   1b) Virginia Group : The Jumbo Virginia or Early Virginia variety has the largest nuts of all the types. This is a common roasting variety that needs between 120 and 130 days to produce a crop.   1c) Tennessee Red Valencia Group: Valencia peanuts are sweet and typically roasted or boiled. This variety produces three or more nuts per pod, and it takes between 120 and 130 days to reach maturity.")
#print(str(s1))

l1 = ['1)Choose which variety of peanuts to plant in your plot of land-- Choose from one of the following Cultivar Groups:', 'incomplete',
'a) Spanish Group (commonly grown in South Africa): Spanish peanuts are most often used to make peanut butter and candy because of their higher oil content. The Spanish variety produces small nuts with a brownish-red skin.  Spanish peanuts need about 90 to 130 days for maturity.','learnmore123',
'1b) Virginia Group : The Jumbo Virginia or Early Virginia variety has the largest nuts of all the types. This is a common roasting variety that needs between 120 and 130 days to produce a crop.','learnmore123',
'1c) Tennessee Red Valencia Group: Valencia peanuts are sweet and typically roasted or boiled. This variety produces three or more nuts per pod, and it takes between 120 and 130 days to reach maturity.','learnmore123','taskbreak']


p_reply='zzz'
count=0
not_done = 0
old_count = 0
while(count<len(l1)):
	if(count%2 == 0):
		print(str(l1[count]))
	if(count%2 == 1):
		if(l1[count] !='learnmore123' and l1[count] != 'taskbreak'):
			print('CURRENT TASK STATUS: '+str(l1[count]))
			p_reply=input("Have you completed this sub-task (y/n): ")
			print('you said: '+str(p_reply))
			if(p_reply == 'y'):
				l1[count] = 'complete'
				print('NEW TASK STATUS:'+str(l1[count]))
			if(l1[count] == 'incomplete'):
				not_done = not_done + 1
				print('Number of sub-tasks still incomplete: '+str(not_done))
	if(l1[count] =='taskbreak'):
		#print('debbbbbbbuuuuuuuuuuuug')
		if(not_done == 0):
			print('all sub-tasks complete-- moving on to next task...')
		else:
			p_reply=input('not all sub-tasks have been completed.  Would you like to move on to the next task anyway? (y/n): ')
			if(p_reply == 'y'):
				old_count = count + 1
				count = old_count - 1
				not_done = 0
			else:
				not_done = 0
				count = old_count - 1
				print('returning to old count now which is: ' + str(count))
	count=count+1


print('program over-- bye!')


#print("full list: " + str(p_list))
