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

a = raw_input("a: ")
b = raw_input("b: ")
c = raw_input("c: ")

a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4 * a * c

if (delta < 0):
    print "Error"
    exit()
    
delta_root = math.sqrt(delta)

# Positive value
positive = (-b + delta_root ) / (2 * a)

# Negative value
negative = (-b - delta_root ) / (2 * a)

print "The quadratic result is %f and %f" % (positive, negative)