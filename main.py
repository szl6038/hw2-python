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

  Course2grade = input("Enter your course 2 letter grade: ")

  Course2credit = input("Enter your course 2 credit: ")

  GP2 = getGradePoint(Course2grade)

  print("Grade point for course 2 is: " +str(GP2))

  Course3grade = input("Enter your course 3 letter grade: ")

  Course3credit = input("Enter your course 3 credit: ")

  GP3 = getGradePoint(Course3grade)

  print("Grade point for course 3 is: " +str(GP3))

  GPC1 = (GP1*float(Course1credit))

  GPC2 = (GP2*float(Course2credit))

  GPC3 = (GP3*float(Course3credit))

  TGPC = (GPC1+GPC2+GPC3)

  TC = (float(Course1credit)+float(Course2credit)+float(Course3credit))

  GPA = (TGPC/TC)
  
  print("Your GPA is: " + str(GPA))
  

if __name__ == "__main__":
  run()
