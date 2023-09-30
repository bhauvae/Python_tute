from tabulate import tabulate


class Students:
    def __init__(self, first_name: str, last_name: str, roll_number: int):
        self.first_name = first_name
        self.last_name = last_name
        self.roll_number = roll_number

    def email_generator(self):
        email_list = {}
        for index in range(number_of_students):
            email_list[self.roll_number] = self.first_name + self.last_name + str(self.roll_number) + "@school.com"

        return email_list[self.roll_number]

    def __str__(self):
        return "\nStudent Data\nRoll Number:: {}\nFull Name:: {} {}\nEmail:: {}".format(self.roll_number,
                                                                                        self.first_name,
                                                                                        self.last_name,
                                                                                        Students.email_generator(self))


class Subjects(Students):
    available_subjects = (("Subject Name", "Subject Code"),
                          ("Maths", 1),
                          ("English", 2),
                          ("Physics", 3),
                          ("Chemistry", 4),
                          ("Physical Education", 5),
                          ("Computer Science", 6))

    def __init__(self, first_name, last_name, roll_number, subject_info):
        super(Students).__init__(first_name, last_name, roll_number)
        self.subject_info = subject_info

    def grade(self):
        marks_total = 0
        for counter in self.subject_info:
            marks_total = marks_total + self.subject_info[counter]

        marks_percentage = marks_total / (len(self.subject_info))

        if marks_percentage > 90:
            return 'A'
        elif 90 >= marks_percentage > 80:
            return 'B'
        elif 80 >= marks_percentage > 70:
            return 'C'
        elif 70 >= marks_percentage > 60:
            return 'D'
        else:
            return 'F'

    def __str__(self):
        return f"\nStudent Data\nRoll Number:: {self.roll_number}\nFull Name:: {self.first_name} {self.last_name}" \
               f"\nEmail:: {Subjects.email_generator(self)}\n" \
               f"Subject Information\n{self.subject_info}\n" \
               f"Grade:: {Subjects.grade(self)}"


def input_student_data(student_count):
    student_data = []

    for counter in range(student_count):
        print("Enter the details for Student ", counter + 1)
        first_name = str(input("enter the first name: "))
        last_name = str(input("enter the last name: "))
        roll_number = int(input("enter the roll number: "))
        student_data.append(Students(first_name, last_name, roll_number))

    return student_data


def input_subject_data(student_count):
    student_data = []
    subject_info = {}
    subject_list = []

    for counter in range(student_count):
        print("Enter the details for Student ", counter + 1)
        first_name = str(input("enter the first name: "))
        last_name = str(input("enter the last name: "))
        roll_number = int(input("enter the roll number: "))

        number_of_subjects = int(input("Enter the number of subjects:: "))

        print("Select the indices for the subjects that the student has:: ")

        print(tabulate(Subjects.available_subjects, headers='firstrow', tablefmt='fancy_grid'))

        for i in range(number_of_subjects):
            s = int(input("Enter the index:: "))
            subject_list.append(Subjects.available_subjects[s][0])
            print("Subject selected:: ", Subjects.available_subjects[s][0])

        print("Enter subject marks")
        for counter2 in range(number_of_subjects):
            subject_info[subject_list[counter2]] = int(input("Enter the marks for {}: ".format(subject_list[counter2])))

        student_data.append(Subjects(first_name, last_name, roll_number, subject_info))

    return student_data


number_of_students = int(input("Enter the number of Students: "))
subject_confirmation = str(input("Do you want to enter subject data (yes or no): "))

if subject_confirmation == 'yes' or subject_confirmation == 'y':
    student_information = input_subject_data(number_of_students)
else:
    student_information = input_student_data(number_of_students)

print(student_information[0])
