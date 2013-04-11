#!/usr/bin/env python

# Copyright (c) 2013 Adam Blackburn
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math

# the execution times, in T1, T2, ..., TI order
exec_times = [2, 10, 9]

# the periods, in T1, T2, ..., TI order
periods = [6, 24, 36]

# the number of processes
process_count = len(exec_times)

# the initial response times
r = []
for i in range(process_count):
    r.append([sum(exec_times[:i + 1])])

print 'execution times', exec_times
print 'periods', periods
print 'process count', process_count
print 'initial response times', r

print

# iterate through each process
for i in range(process_count):
    print 'task', i + 1

    # track the iteration number
    k = 0

    # as long as the response time is smaller than the period, keep going
    while r[i][k] <= periods[i]:
        # calculate the sum for this iteration
        j = 0
        sum = 0
        for j in range(i):
            sum += int(math.ceil(
                    float(r[i][-1]) / float(periods[j])) * exec_times[j]
                )
        sum += exec_times[i]

        # save the response time in the list of response times
        r[i].append(sum)

        # increment the iteration counter
        k += 1

        # print some information about this iteration
        print 'sum', sum, 'period', periods[i]

        # check if task is scheduable
        if r[i][k] == r[i][k - 1]:
            print 'schedulable'
            break

    else:
        # if we didn't leave the while loop via the break,
        # then the task isn't scheduable
        print 'unschedulable'

    print

# print the response times
print 'response times', r
