import array as arr

stressArray = arr.array('i')
depressionArray = arr.array('i')
anxietyArray = arr.array('i')

def calculateSum(arr):
  sum = 0
  for i in range(0, len(arr)):
    sum = sum + arr[i]
  return sum*2