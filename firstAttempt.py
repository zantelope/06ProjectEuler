
###function to calculate sum of n**2 in range (n + 1)
def sumOfSquares(n):

  listSquares = [n ** 2 for n in range(n+1)]
  return sum(listSquares)

  return listSquares

###function to calculate square of sum for n in range (n + 1)
def squareOfSum(n):
  numList = [n for n in range(n + 1)]
  return sum(numList) ** 2

### function to determine difference between sum of squares and square of sum
def difference(n):

  return abs(squareOfSum(n) - sumOfSquares(n))

n = 100

print(difference(100))
