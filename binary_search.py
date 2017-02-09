class BinarySearch(list):
  """Implementation of binary search"""

  def __init__(self, a, b):
      """Create a list of length a and step b"""

      list.__init__(self)
      self.length = a
      first = b
      last = a * b
      while first <= last:
          self.append(first)
          first += b

  def search(self, number):
      found = False
      first = 0
      last = self.length - 1
      middle = (first + last) // 2
      count = 0

      if (number == self[first]) or (number== self[last]) \
          or (number == self[middle]):
          return {
              'count': count,
              'index': self.index(number)
          }
      if self.count(number) == 0:
        return {
            'count': 3,
            'index': -1
            }
      else:
        while first < last and not found:

            middle = (first + last) // 2

            if number == self[middle]:
              found = True
            else:
              count += 1
              if number > self[middle]:
                  first = middle + 1
              else:
                  last = middle - 1

        if found:
          return {
              'count': count,
              'index': self.index(number)
          }
        else:
          return {
              'count': count,
              'index': -1
          }
