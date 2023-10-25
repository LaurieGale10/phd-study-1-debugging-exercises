import unittest
#Step 1: Get program in JSON form
#Step 2: Do initial checks e.g. does it differ from original?
#Step 3 (if program doesn't require output): Run it; check its output
program = 'width = 50\ndepth = 25\nheight = depth\nvolume = height * width * depth\nprint("The volume is,volume")'
exec(program)

