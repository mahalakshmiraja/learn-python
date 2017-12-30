grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  sum_grade=0
  for i in scores:
      sum_grade += i
  print (sum_grade)
  return sum_grade




def average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    avg= sum_of_grades/float(len(grades_input))
    print ('The average of grades is %d '%round(avg))
    return avg

average(grades)