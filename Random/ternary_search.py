'''Same as binary search but divide the problem in to three parts'''

def ternary_search (L, key):
        left = 0
        right = len(L) - 1
        while left <= right:
           ind1 = left
           ind2 = left + (right - left) // 3
           ind3 = left + 2 * (right - left) // 3
           n = 0

           if key == L[left]:
              n += 1
              print("Checking if " + str(key) + " is equal to " + str(left))
              print("Search successful")
              print(str(key) + " is located at index " + str(left))
              print("A total of " + str(n) + " comparisons were made")
              return

           elif key == L[right]:
              n += 1
              print("Checking if " + str(key) + " is equal to " + str(right))
              print("Search successful")
              print(str(key) + " is located at index " + str(right))
              print("A total of " + str(n) + " comparisons were made")
              return

           elif key < L[left] or key > L[right]:
              n += 1
              print("Search not successful")
              print("A total of " + str(n) + " comparisons were made")
              return

           elif key <= L[ind2]:
              n += 1
              print("Checking if " + str(key) + " is less than " + str(L[ind2]))
              right = ind2 -1

           elif key > L[ind2] and key <= L[ind3]:
              n += 1
              print("Checking if " + str(key) + " is less than " + str(L[ind2]))
              print("Checking if " + str(key) + " is equal to " + str(L[ind3]))
              print("Checking if " + str(key) + " is less than " + str(L[ind3]))         
              left = ind2 + 1
              right = ind3

           else:
              n += 1
              print("Checking if " + str(key) + " is less than " + str(L[ind3]))         
              left = ind3 + 1

        return

def ternary_search1(L, key):
   left = 0
   right = len(L) - 1
   while left <= right:
      ind1 = left
      ind2 = left + (right - left) // 3
      ind3 = left + 2 * (right - left) // 3
      if key == L[left]:
         print("Key found at:" + str(left))
         return
      elif key == L[right]:
         print("Key found at:", str(right))
         return
      elif key < L[left] or key > L[right]:
         print("Unable to find key")
         return
      elif key <= L[ind2]:
         right = ind2
      elif key > L[ind2] and key <= L[ind3]:
         left = ind2 + 1
         right = ind3
      else:
         left = ind3 + 1
   return

ternary_search([6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94], 51)
ternary_search1([6,12,18,22,29,37,38,41,51,53,55,67,73,75,77,81,86,88,94],88)