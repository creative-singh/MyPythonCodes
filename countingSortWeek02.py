# Counting Sort - Week 02 - Day 05
#given_list - [1,1,3,2,1]
given_list = [1,1,3,2,1]
final_list = []                  #this is blank list which will contain sorted list 
maxVal = max(given_list)         #this will take out maximum value from given_list
process_list = [0]*(maxVal+1)    #this will create [0,0,0,0]
for i in given_list:             #this for loop count the number of occurence of 
    process_list[i]+=1              #a number in given_list 
count=0
for val in process_list:         #taking value from process list and copyieng it to
    while val > 0:                  #final_list through loops
        final_list.append(count)
        val-=1
    count+=1
print(f'Given list is : {given_list}')
print(f'Sorted list is : {final_list}')

