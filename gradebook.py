last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
subjects = ["physics", "calculus", "poetry", "history"]

#grades list
grades = [98, 97, 85, 88]

#two-dimensional list
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

#appending new subject and score
gradebook.append(["computer science", 100])

#appending another visual arts
gradebook.append(["visual arts", 93])

#modifying visual arts score
gradebook[-1][-1] = 98 

#removing poetry grade
gradebook[2].remove(85)

#changing poetry grade to "Pass"
gradebook[2].append("Pass")
