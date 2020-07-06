# This script can be used for testing a students code, where example is the module to be tested.
# Further items that could be added could be timers to check the speed taken to run to see if
# the code runs in the required time
# @author dave-t-c

# Copyright 2020 dave-t-c
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or other
# materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its contributors may be used
# to endorse or promote products derived from this software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import sys


def check_script():
    # See if the student has given the module the correct name so it can be imported.
    try:
        import searches
    except ModuleNotFoundError:
        print("Could not find the script. Did you make sure to call it: 'searches'?")
        sys.exit(1)

    # Check if the method being tested exists in the script
    if not dir(searches).__contains__('linearsearch'):
        print("Could not find the function called 'linearsearch', did you give it the correct name?")
        sys.exit(2)

    # Check if the method returns the expected value.
    # This can be changed to whatever type / structure required.
    # The function can also take any required parameters
    # More methods can be checked if required.
    expected_value = False
    value = 99
    params = [5, 10, 20, 2, 7, 18, 34, 98]
    returned_val = searches.linearsearch(params, value)
    if returned_val != expected_value:
        print("The function did not return the correct result with params: " + str(params))
        print("It returned: " + str(returned_val) + " instead of: " + str(expected_value))
        sys.exit(3)

    # If it has returned the expected value then the method has passed the test
    print("Passed all tests!")
    sys.exit(0)


check_script()
