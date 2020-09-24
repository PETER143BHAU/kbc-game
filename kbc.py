print('                                           k.b.c')
print('                                           *******')
print('                                       welcome to k.b.c')
print('                                       ******************')
a=input('                ARE  U READY TO START :: Y/N  :: ')
while 1:
	if a=='y':
		print('ok lets START')
	elif a=='n':
		print('o')
		break
		
	print('                           QUESTIONS')
	ques=['Q1:: Where is navgurukul located ?','Q2:: Aap waha par kis cheej ka course karte hain?','Q3:: Waha ka co-founder kon hain?','Q4:: Dharamshala camps main kitne bache rehte hain ?','Q5::Vaha ke coming governer kon hain ?']
	op=['1::DELHI \n 2::PUNJAB \n 3::AGRA\n 4::DHARAMSHALA','1::CHEF \n 2::MANAGER \n 3::SOFTWARE ENGINEERING \n 4::INDIAN ARMY','1::KUMAR NAYAK \n 2::ABHISHEK GUPTA \n 3::NITESH \n 4::SURBHI','1::60 \n 2::20 \n 3::30 \n 4::50','1::ATUL \n 2::AMAN \n 3::NAYAK \n 4::RAHIT']
	d=[4,3,2,1,3]
	g=[1,4,3,3,1]
	a=0
	s=0
	nm=0
	count=0
	t=True
	for i in ques:
		print(i,'\n',op[a])
		a+=1
		f=input('enter do you want 50-50 life line   yes/no  ')
		if f=='yes':
			print('it is between',g[nm],'and',d[s])
			nm+=1
		else:
			print('its ok than enter number')

		b=int(input('enter any number  '))
		if b==d[s]:
			s+=1
			print('it is CORRECT')
		else:
			print('it is not CORRECT','\n','SORRY','\n','YOU ARE NOT IN KBC YOU ARE OUT')
			t=False
			break
		if b==d:
			print('you got nothing')
		else:
			print('you got 5000,rupees')

	if t==False:
		break
	break


	

	
	


	




	
	
	

# print(q1[1])
# for i in op1[1]:

# 	print(i)
# s=input('ENTER THE CORRECT ANSWER ')
# if s=='3':
# 	print('it is CORRECT')
# else:
# 	print('it is not CORRECT')

# print(q1[2])
# for i in op1[2]:

# 	print(i)
# s=input('ENTER THE CORRECT ANSWER ')
# if s=='3':
# 	print('it is CORRECT')
# else:
# 	print('it is not CORRECT')

# print(q1[3])
# for i in op1[3]:

# 	print(i)
# s=input('ENTER THE CORRECT ANSWER ')
# if s=='3':
# 	print('it is CORRECT')
# else:
# 	print('it is not CORRECT')

# print(q1[4])
# for i in op1[4]:

# 	print(i)
# s=input('ENTER THE CORRECT ANSWER ')
# if s=='3':
# 	print('it is CORRECT')
# else:
# 	print('it is not CORRECT')




		




