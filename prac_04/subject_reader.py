"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and print neatly"""
    subjects = get_subjects()
    print(subjects)
    print_subjects(subjects)


def get_subjects():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject.append(parts)
    input_file.close()
    return subject


def print_subjects(subjects):
    """print data nicely"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()