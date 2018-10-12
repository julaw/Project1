import os
import filecmp
from dateutil.relativedelta import *
from datetime import date

file= 'p1DataA.csv'


#get a list of dictionary objects from the file
# #Input: file name
# #Ouput: return a list of dictionary objects where
# #the keys are from the first row in the data. and the values are each of the other rows
def getData(file=file):
	# open the file
	infile=open(file,'r')
	lines=infile.readlines()[1:]
	infile.close()
	data = []
	for line in lines:
		dictstudents={}
		line = line.rstrip()
		line=line.split(',')
		fname=line[0]
		lname=line[1]
		email=line[2]
		grade=line[3]
		DOB=line[4]
		dictstudents['First']=fname
		dictstudents['Last']=lname
		dictstudents['Email']=email
		dictstudents['Class']=grade
		dictstudents['DOB']=DOB
		data.append(dictstudents)
	return data




def mySort(data,col):
	sorteddata= sorted(data, key=lambda x:x[col])
	return sorteddata[0]['First']+' '+ sorteddata[0]['Last']

mySort(getData(file),'First')

# # Sort based on key/column
# #Input: list of dictionaries and col (key) to sort on
# #Output: Return the first item in the sorted list as a string of just: firstName lastName
#
#
#

data=getData(file)


def classSizes(data):
	freshmancount=0
	sophomorecount=0
	juniorcount=0
	seniorcount=0

	for studentdict in data:
		if studentdict['Class']== "Freshman":
			freshmancount+=1
		elif studentdict['Class'] =="Sophomore":
			sophomorecount+=1
		elif studentdict['Class']=='Junior':
			juniorcount+=1
		else:
			seniorcount+=1
	listoftuples=[('Senior', seniorcount), ('Junior', juniorcount), ('Sophomore', sophomorecount), ('Freshman', freshmancount)]
	sortedlistoftuples=sorted(listoftuples, key=lambda x:x[1], reverse=True)
	return sortedlistoftuples


# # Create a histogram
# # Input: list of dictionaries
# # Output: Return a list of tuples sorted by the number of students in that class in
# # descending order
# # [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

def findMonth(data):
	months={}
	for dictionary in data:
		month=dictionary['DOB'].split('/')[0]
		months[month]=months.get(month,0)+1
	monthssorted= sorted(months, key=months.get, reverse=True)
	return int(monthssorted[0])

print(findMonth(data))

# # Find the most common birth month form this data
# # Input: list of dictionaries
# # Output: Return the month (1-12) that had the most births in the data
#

def mySortPrint(data,col,fileName):

	sorteddata= sorted(data, key=lambda x:x[col])
	return sorteddata[0]['First']+' '+ sorteddata[0]['Last']


# #Similar to mySort, but instead of returning single
# #Student, the sorted data is saved to a csv file.
# # as fist,last,email
# #Input: list of dictionaries, col (key) to sort by and output file name
# #Output: No return value, but the file is written
#
# 	pass
#
# def findAge(a):
# # def findAge(a):
# # Input: list of dictionaries
# # Output: Return the average age of the students and round that age to the nearest
# # integer.  You will need to work with the DOB and the current date to find the current
# # age in years.
#look up date() on stack overflow
#
# 	pass
#
#
# ################################################################
# ## DO NOT MODIFY ANY CODE BELOW THIS
# ################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)
#
	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
