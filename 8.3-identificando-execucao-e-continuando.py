
l = [1, 3, 4]

try:
    print l[12]
except IndexError, error:
    print 'Error: %s' % errorS