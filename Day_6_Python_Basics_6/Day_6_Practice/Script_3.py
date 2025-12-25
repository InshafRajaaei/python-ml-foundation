# Script 3: The CSV Analyzer (Manual Parsing)
# Goal: Calculate stats from a file.

# 1. Create grades.csv with this content:

# Subject,Score
# Math,90
# Science,85
# History,70
# English,95

# 2. Open the file using open().
# 3. Skip the header.
# 4. Loop through lines, split them, and extract the score (convert to int).
# 5. Calculate the Average Score.
# 6. Print: "Average Grade: [Value]".

with open("grades.csv", "r") as fl:
    header = fl.readline()
    total_score = 0
    subject_count = 0
    for line in fl:
        clean_line = line.strip()   #removing whitspace,newline
        row = clean_line.split(",") #split by commas into a list
        scores = int(row[1])
        total_score += scores
        subject_count += 1
    if subject_count == 0:
        print("No grades found.")
    else:
        avrg = total_score/subject_count
        print(f"Average Grade: {avrg}")
   
# Blind trust in CSV structure
# This line:

# scores = int(row[1])

# Assumes:
#   every line has 2 columns
#   score is always a valid integer
# One bad row → program dies.
# For learning, fine. For real code, unacceptable

# with open("grades.csv", "r", encoding="utf-8") as fl:
#     fl.readline()  # skip header

#     total_score = 0
#     subject_count = 0

#     for line in fl:
#         subject, score = line.strip().split(",")
#         total_score += int(score)
#         subject_count += 1

#     if subject_count > 0:
#         average = total_score / subject_count
#         print(f"Average Grade: {average}")
#     else:
#         print("No grades found.")\

# Same Logic code but more Cleaner Safer
