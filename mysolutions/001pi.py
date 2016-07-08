# find pi to the n-th digit
import math
def pi(digits):
  limit = 100
  if digits > limit:
    digits = limit
  digits = int(digits)
  return format(math.pi, '.' + str(digits) + 'f')
