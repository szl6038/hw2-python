def getGradePoint(lettergrade):
  if lettergrade=="A":
    point = float(4.0)
  elif lettergrade=="A-":
    point = float(3.67)
  elif lettergrade=="B+":
    point = float(3.33)
  elif lettergrade=="B":
    point = float(3.0)
  elif lettergrade=="B-":
    point = float(2.67)
  elif lettergrade=="C+":
    point = float(2.33)
  elif lettergrade=="C":
    point = float(2.0)
  elif lettergrade=="D":
    point = float(1.0)
  else:
    point = float(0)
  
  return point

def run():
  
  Course1grade = input("Enter your course 1 letter grade: ")

  Course1credit = input("Enter your course 1 credit: ")

  GP1 = getGradePoint(Course1grade)

  print("Grade point for course 1 is: " +str(GP1))



  

if __name__ == "__main__":
  run()
