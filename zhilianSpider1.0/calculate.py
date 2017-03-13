#encoding=utf-8
from pandas import DataFrame,Series
list_language = ['perl','ruby','vb','javascript','verilog','html','python','php','c','java','objective-c']
rank = [0]*20
list_rank = ['0-2k','2-4k','4-6k','6-8k','8-10k','10-12k','12-14k','14-16k','16-18k','18-20k','20-22k','22-24k','24-26k','26-28k','28-30k','30-32k','32-34k','34-36k','36-38k','>38k']
dict_rank = {'perl':[0]*20,'ruby':[0]*20,'vb':[0]*20,'javascript':[0]*20,'verilog':[0]*20,'html':[0]*20,'python':[0]*20,'python':[0]*20,'php':[0]*20,'c':[0]*20,'java':[0]*20,'objective-c':[0]*20}
dict_average = {'perl':0,'ruby':0,'vb':0,'javascript':0,'verilog':0,'html':0,'python':0,'python':0,'php':0,'c':0,'java':0,'objective-c':0}
dict_count   = {'perl':0,'ruby':0,'vb':0,'javascript':0,'verilog':0,'html':0,'python':0,'python':0,'php':0,'c':0,'java':0,'objective-c':0}


for language in list_language:
	Sum = 0
	Count = 1
	p = 0
	fl = open('/root/zhilian/language/'+language+'.txt','r')
	for s in fl:
		s = s.rstrip('\n')
		s = s.split('|')
		if(s[-2][-4] != '/'):
			continue
		salary = s[-2]
		salary = salary.split('-')
		salary_low = int(salary[0][15:])
		salary_high = int(salary[1][:-7])
		salary_mid = (salary_low + salary_high)/2
#		if salary_mid > 40000:
#	print language,salary_low,salary_high
		if( salary < 1000  ):
			continue
		if (0 < salary_mid < 2000):
			dict_rank[language][0] = dict_rank[language][0] + 1
		elif(2000 <= salary_mid < 4000):
			dict_rank[language][1] = dict_rank[language][1] + 1
		elif(4000 <= salary_mid < 6000):
			dict_rank[language][2] = dict_rank[language][2] + 1
		elif(6000 <= salary_mid < 8000):
			dict_rank[language][3] = dict_rank[language][3] + 1
		elif(8000 <= salary_mid < 10000):
			dict_rank[language][4] = dict_rank[language][4] + 1
		elif(10000 <= salary_mid < 12000):
			dict_rank[language][5] = dict_rank[language][5] + 1
		elif(12000 <= salary_mid < 14000):
		 	dict_rank[language][6] = dict_rank[language][6] + 1
		elif(14000 <= salary_mid < 16000):
			dict_rank[language][7] = dict_rank[language][7] + 1
		elif(16000 <= salary_mid < 18000):
			dict_rank[language][8] = dict_rank[language][8] + 1
		elif(18000 <= salary_mid < 20000):
			dict_rank[language][9] = dict_rank[language][9] + 1
		elif(20000 <= salary_mid < 22000):
			dict_rank[language][10] = dict_rank[language][10] + 1
		elif(22000 <= salary_mid < 24000):
			dict_rank[language][11] = dict_rank[language][11] + 1	
		elif(24000 <= salary_mid < 26000):
			dict_rank[language][12] = dict_rank[language][12] + 1
		elif(26000 <= salary_mid < 28000):
			dict_rank[language][13] = dict_rank[language][13] + 1
		elif(28000 <= salary_mid < 30000):
			dict_rank[language][14] = dict_rank[language][14] + 1
		elif(30000 <= salary_mid < 32000):
			dict_rank[language][15] = dict_rank[language][15] + 1
		elif(32000 <= salary_mid < 34000):
			dict_rank[language][16] = dict_rank[language][16] + 1
		elif(34000 <= salary_mid < 36000):
			dict_rank[language][17] = dict_rank[language][17] + 1
		elif(36000 <= salary_mid < 38000):
			dict_rank[language][18] = dict_rank[language][18] + 1
		elif(38000 <= salary_mid ):
			dict_rank[language][19] = dict_rank[language][19] + 1

		Sum = Sum + salary_mid
#	print i,':',salary_low,salary_high,salary_mid
		Count = Count + 1

	Average = Sum / Count
#dict_rank[language] = rank
	dict_average[language] = Average
	dict_count[language] = Count


print '=========================================================='
print 'rank'
frame_rank = DataFrame(dict_rank)

frame_rank.to_csv('/root/zhilian/csv/frame_rank.csv')

print '=========================================================='
print 'average'
dict_average = {'average':dict_average}
frame_average = DataFrame(dict_average)
print frame_average
frame_average.to_csv('/root/zhilian/csv/frame_average.csv')
print '=========================================================='
print 'count'


Sum1 = 0
i = 0
list_quart = [0]*20
dict_quart = {'perl':0,'ruby':0,'vb':0,'javascript':0,'verilog':0,'html':0,'python':0,'python':0,'php':0,'c':0,'java':0,'objective-c':0}

for language in list_language:
	Sum1 = Sum1 + dict_count[language]

for language in list_language:
	quart = dict_count[language]*1.0/Sum1
	list_quart[i] = quart
	i = i + 1
	dict_quart[language] = quart
print 'list_quart:',list_quart
#print 'dict_quart:',dict_quart


dict_count = {'count':dict_count}
frame_count = DataFrame(dict_count)
print frame_count
frame_count.to_csv('/root/zhilian/csv/frame_count.csv')
