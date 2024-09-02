from collections import Counter 

class Solution:
  def getSequence(self, dna):
    res = []
    for dna1, dna2 in dna:
      res.append(self.can_be_anagram(dna1, dna2))
    return res

  def can_be_anagram(self, s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    count1 = 0
    count2 = 0
    for key in s1.keys():
      if key not in s2:
        count1 += 1
      elif s1[key] > s2[key]:
        count1 += 1
      if count1 > 1: 
        return False

    for key in s2.keys():
      if key not in s1:
        count1 += 1
      elif s1[key] < s2[key]:
        count2 += 1
      if count2 > 1:
        return False
      
    return True