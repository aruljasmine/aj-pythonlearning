def get_grade(student):
    marks = student["marks"]

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


student1 = {"name": "Jas", "marks": 85}

print(student1["name"], get_grade(student1))