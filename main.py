#Find Intersection
#Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: 
#the first element will represent a list of comma-separated numbers sorted in ascending order, 
#the second element will represent a second list of comma-separated numbers (also sorted). 
#Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. 
#If there is no intersection, return the string false.

#Examples
#Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
#Output: 1,4,13

#Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
#Output: 1,9,10








def FindIntersection(strArr):
  
  # code goes here
  data = []
  datastring = ""
  
  value1 = strArr[0].split(',')
  value2 = strArr[1].split(',')

  value1 = [int(num_string) for num_string in value1]
  value2 = [int(num_string) for num_string in value2]

  for i in value1:    
    if i in value2:
      data.append(i)
      
      if len(data) <= 1:
        datastring = "{}".format(i)
      else:
        datastring = "{},{}".format(datastring,i)

  print(datastring)
  return data

# keep this function call here 
print FindIntersection(raw_input())
