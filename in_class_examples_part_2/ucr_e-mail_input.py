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


# Get first and last name and number from user.
first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
number = raw_input("Enter a number: ")

# Normalize the input.
first_name = first_name.lower()
last_name = last_name.lower()
int_number = int(number)

# Create UCR Net ID
net_id = "{0}{1}{2:03d}".format(first_name[0], last_name[0:4], int_number)

# Print the UCR Net ID
print "Your UCR Net ID is {0}.".format(net_id)