import sys

output = open(sys.argv[1] + '.fixed.pkl', 'w', newline='\n')
output.write(open(sys.argv[1], 'r').read())