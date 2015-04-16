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
# Tip Calculator
#
# We are going to use the bill, tax rate, and tip percentage to calculate the total.
#

print "Lets calculate the total bill with tip."

# Get bill about from user.
bill = 10.25

# Define tax and tip amount.
tax_rate = 0.09
tip_perc = 0.20

# Calculate total meal cost and show the value to the user.
bill_total = bill * (1 + tax_rate)
print "Bill with tax: ${0:0.2f}".format(bill_total)

# Calculate total meal with tip cost and show the value to the user.
tip = bill_total * tip_perc
print "tip: $" + str(tip)
print "Total bill: $" + str(bill_total + tip)

