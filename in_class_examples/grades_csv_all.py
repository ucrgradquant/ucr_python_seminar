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

def score_to_grade(average):
        # Find Adam's letter grade
        if average > 0.90:
                return "A"
        elif average > 0.80:
                return "B"
        elif average > 0.70:
                return "C"
        elif average > 0.60:
                return "D"
        else :
                return "F"

# Define constants
STUDENT_ID_INDEX = 0
NAME_INDEX = 1
ASSIGNMENT_INDEX = 3
SCORE_INDEX = 4
TOTAL_INDEX = 5

score = dict()
total = dict()

import csv
with open('grades.csv', 'rb') as csvfile:
    grade_reader = csv.reader(csvfile)
    for row in grade_reader:
        if not score.has_key(row[STUDENT_ID_INDEX]):
             score[row[STUDENT_ID_INDEX]] = 0
        if not total.has_key(row[STUDENT_ID_INDEX]):
             total[row[STUDENT_ID_INDEX]] = 0
        score[row[STUDENT_ID_INDEX]] += int(row[SCORE_INDEX])
        total[row[STUDENT_ID_INDEX]] += int(row[TOTAL_INDEX])
        
print score
print total

for student_id in score.keys():
    if total.has_key(student_id):
        average = float(score[student_id]) / total[student_id]
        print student_id, score_to_grade(average)


