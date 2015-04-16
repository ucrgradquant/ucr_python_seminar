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
# Quadratic Equation
import math

print "Lets calculate the Quadratic Equation."

# Get the values from the user.
a = 1
b = 9
c = 2

# Apply formula.
b24ac = b**2 - 4 * a * c

if (b24ac < 0):
    print "negative value"
    exit()


# postive formula
pos_value = (-b + math.sqrt(b24ac)) / (2 * a)

# negative formula
neg_value = (-b - math.sqrt(b24ac)) / (2 * a)

# Print out the result
string_result = """Quadratic equation for (a={0}, b={1}, c={2})
the positive result is {3} and the negative result is {4}"""
print string_result.format(a,b,c,pos_value, neg_value)