# find e to the n-th digit
import math
def find_e(digits):
  limit = 100
  if digits > limit:
    digits = limit
  digits = int(digits)
  return format(math.e, '.' + str(digits) + 'f')
