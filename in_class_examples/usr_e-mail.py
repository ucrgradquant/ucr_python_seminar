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
# Calculate the persons UCR Net ID.

student_names = [
        "Adam Jones",
        "Beth Smith",
        "Caleb Kim",
        "Danny Jacobs",
        "Eric Jones",
    ]
    
print student_names

# constants
FIRST_NAME_INDEX = 0
LAST_NAME_INDEX = 1

# For each student
for name in student_names:
        name = name.lower()
        # Find the first and last name
        name_split = name.split(" ")

        # Print Create UCR ID
        print "%s%s%03d"%(name_split[FIRST_NAME_INDEX][0], \
                name_split[LAST_NAME_INDEX][0:4], 1)


# Two String methods: split, lower