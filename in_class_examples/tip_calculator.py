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

bill = raw_input("Bill amount: ")
bill = float(bill)

tax = 0.0875

tip = 0.18

meal = bill + bill * tax

print "Meal total: %.2f" % meal

total = meal + meal * tip

print "Total with tip: %.2f" % total