#
# Copyright 2009-2013 by The Regents of the University of California
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# you may obtain a copy of the License from
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Calculate the students grades.
#
# Here is a list of individual grade records.
#  - Name, Assignment #, Score, Total

grades_file = open("grades_emily.csv") 

emily_grades = [] # list of assignments
for line in grades_file:
    # update emily_grades
    emily_grades.append(line.strip().split(","))

grades_file.close()

# print emily_grades
# exit()

# Define constants
NAME_INDEX = 1
ASSIGNMENT_INDEX = 3
SCORE_INDEX = 4
TOTAL_INDEX = 5

# Find Emily's average score
score = 0
total = 0
for row in emily_grades:
        score = score + int(row[SCORE_INDEX])
        total += int(row[TOTAL_INDEX])

average = float(score) / total
print average
print type(average)


def score_to_grade(average):
        # Find Adam's letter grade
        if average > 0.90:
                print "A"
        elif average > 0.80:
                print "B"
        elif average > 0.70:
                print "C"
        elif average > 0.60:
                print "D"
        else :
                print "F"

score_to_grade(average)