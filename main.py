# Author: Jasmine Sandhu jps6818@psu.edu
# Collaborator:Carl Foust czf276@psu.edu
# Collaborator: Nathan Donahue ndd5167@psu.edu 
# Collaborator: Nick Orf nco5067@psu.edu
# Section: 10
# Breakout: 4

def getLetterGrade(grade):
  grade = float(grade)
  if (grade >= 93.0):
    return "A"
  elif ((90.0 <= grade) & (grade < 93.0)):
    return "A-"
  elif ((87.0 <= grade) & (grade < 90.0)):
    return "B+"
  elif ((83.0 <= grade) & (grade < 87.0)):
    return "B"
  elif ((80.0 <= grade) & (grade < 83.0)):
    return "B-"
  elif ((77.0 <= grade) & (grade < 80.0)):
    return "B"
  elif ((70.0 <= grade) & (grade < 77.0)):
    return "C"
  elif ((60.0 <= grade) & (grade < 70.0)):
    return "C-"
  else:
    return "F" 

def run():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = getLetterGrade(grade)
  print(f"Your letter grade for CMPSC 131 is {grade}." )

if __name__ == "__main__":
  run()



