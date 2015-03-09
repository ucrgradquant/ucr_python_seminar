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

adam_grades = [
        ["Adam", 1, 9, 10],
        ["Adam", 2, 8, 10],
        ["Adam", 3, 9, 10],
        ["Adam", 4, 7, 10],
        ["Adam", 5, 5, 10],
    ]
    
# Define constants
NAME_INDEX = 0
ASSIGNMENT_INDEX = 1
SCORE_INDEX = 2
TOTAL_INDEX = 3

# Find Adam's average score
score = 0
total = 0
for row in adam_grades:
        score = score + row[SCORE_INDEX]
        total += row[TOTAL_INDEX]

average = float(score) / total
print average
print type(average)

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

