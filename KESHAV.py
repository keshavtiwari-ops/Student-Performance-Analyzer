from array import array

print("=" * 40)
print("     STUDENT PERFORMANCE ANALYZER")
print("=" * 40)

name = input("Enter name: ")
roll = input("Enter roll number: ")

subjects = ["Maths", "Physics", "Chemistry", "Python", "English"]
marks = array('f')

print("\nEnter marks:")

for i in range(5):
    x = float(input(subjects[i] + ": "))
    marks.append(x)

attendance = float(input("Enter attendance: "))
assignment = float(input("Enter assignment percentage: "))


def total():
    t = 0
    for x in marks:
        t = t + x
    return t


def average():
    return total() / 5


def highest():
    high = marks[0]
    high_sub = subjects[0]

    for i in range(1, 5):
        if marks[i] > high:
            high = marks[i]
            high_sub = subjects[i]

    return high_sub, high


def lowest():
    low = marks[0]
    low_sub = subjects[0]

    for i in range(1, 5):
        if marks[i] < low:
            low = marks[i]
            low_sub = subjects[i]

    return low_sub, low


def find_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


def find_performance(avg):
    if avg >= 85:
        return "Excellent"
    elif avg >= 70:
        return "Good"
    elif avg >= 50:
        return "Average"
    else:
        return "Poor"


def attendance_status():
    if attendance < 75:
        return "High Risk"
    elif attendance < 85:
        return "Medium Risk"
    else:
        return "Low Risk"


def academic_status(avg):
    if avg < 50:
        return "High Risk"
    elif avg < 65:
        return "Medium Risk"
    else:
        return "Low Risk"


def get_tips(avg, weak):
    tips = []

    if avg < 70:
        tips.append("Study more.")

    if attendance < 75:
        tips.append("Improve attendance.")

    if assignment < 70:
        tips.append("Complete assignments on time.")

    tips.append("Focus more on " + weak)

    return tips


total_marks = total()
avg = average()

best_subject, best_mark = highest()
weak_subject, weak_mark = lowest()

grade = find_grade(avg)
performance = find_performance(avg)

attendance_risk = attendance_status()
academic_risk = academic_status(avg)

tips = get_tips(avg, weak_subject)


print("\n" + "=" * 40)
print("           STUDENT REPORT")
print("=" * 40)

print("Name       :", name)
print("Roll No.   :", roll)

print("\nMarks:")
for i in range(5):
    print(subjects[i], ":", marks[i])

print("\nPerformance:")
print("Total      :", total_marks, "/ 500")
print("Average    :", round(avg, 2), "%")
print("Grade      :", grade)
print("Result     :", performance)

print("\nHighest Mark:")
print(best_subject, "-", best_mark)

print("Lowest Mark:")
print(weak_subject, "-", weak_mark)

print("\nOther Details:")
print("Attendance :", attendance, "%")
print("Assignment :", assignment, "%")

print("\nRisk:")
print("Attendance :", attendance_risk)
print("Academic   :", academic_risk)

print("\nRecommendations:")
for i in range(len(tips)):
    print(i + 1, ".", tips[i])

print("\nFinal Status:")

if avg >= 50 and attendance >= 75:
    print("ELIGIBLE")
else:
    print("NEEDS IMPROVEMENT")

print("=" * 40)