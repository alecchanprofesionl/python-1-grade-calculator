def grades_please():
# Most words are shortened, "tot" is short for total    
    labs = float(input("Enter the number of labs completed: "))
    quizzes = float(input("Enter the number of quizzes completed: "))

    lab_tot = (labs / 6) * 20
    if lab_tot >= 20:
        lab_tot = 20
    quiz_tot = (quizzes / 6) * 15
    if quiz_tot >= 15:
        quiz_tot = 15

    assi_1 = float(input("Enter grade for Assignment 1: "))
    assi_2 = float(input("Enter grade for Assignment 2: "))
    assi_3 = float(input("Enter grade for Assignment 3: "))
    assi_4 = float(input("Enter grade for Assignment 4: "))

    assi_tot = ((assi_1 + assi_2 + assi_3 + assi_4) / 4) * 0.16

    mid_1 = float(input("Enter grade for Midterm 1: "))
    mid_2 = float(input("Enter grade for Midterm 2: "))

    mid_tot = ((mid_1 + mid_2) / 2) * 0.25

    final = float(input("Enter grade for Final Exam: "))

    final_tot = (final) * 0.18

    midfin = float(input("Enter grade for Midterms and Final Preparation: "))

    midfin_tot = (midfin) * 0.06

    grade_tot = lab_tot + quiz_tot + assi_tot + mid_tot + final_tot + midfin_tot
#idk if I should round or not, but big numbers didnt look nice so i did
    print(f"Your grade is: {grade_tot:.2f}%")
#I removed this since i though it would mess stuff up    
#print("If you don't like it, you should've tried harder (: ")

grades_please()

