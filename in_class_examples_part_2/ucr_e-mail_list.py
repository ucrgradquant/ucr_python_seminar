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
    
# Print each student's UCR Net ID
int_number = 0
for name in student_names:

    # Find the first and last name
    names = name.split()

    # Normalize input
    first_name = names[0].lower()
    last_name = names[1].lower()
    int_number = int_number + 1

    # Create UCR Net ID
    net_id = "{0}{1}{2:03d}".format(first_name[0], last_name[0:4], int_number)
    
    # Print the student's UCR Net ID
    print "{0} UCR Net ID is {1}.".format(name, net_id)