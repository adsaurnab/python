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

def raw_input():
    return ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]

# keep this function call here 
print FindIntersection(raw_input())
