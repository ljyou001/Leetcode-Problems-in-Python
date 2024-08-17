import collections

class Solution:
  def findEncryptedPassword(self, password: str) -> str:
    if len(password) < 2:
      return password

    res = [''] * len(password)
    left = 0
    right = len(password) - 1
    password = collections.Counter(password)

    for char in sorted(password.keys()):
      num = password[char]
      if num % 2 != 0:
        res[len(res) // 2] = char
        num -= 1
      while num > 0 and left < right:
        res[left] = char
        res[right] = char
        left += 1
        right -= 1
        num -= 2
    
    return ''.join(res)