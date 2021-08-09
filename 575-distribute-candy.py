class Solution:
    def distributeCandies2(self, candyType: List[int]) -> int:
    # O(n^2) time? because it's searching through candyTypesEaten each time 
      counter = 0
      candyTypesEaten = []
      remaining = len(candyType) / 2
      for current_candy in candyType:
        if current_candy not in candyTypesEaten and remaining != 0:
          remaining -= 1
          counter += 1
          candyTypesEaten.append(current_candy)
      return len(candyTypesEaten)

    def distributeCandies3(self, candyType: List[int]) -> int:
        # O(n) time where n is the len(candyType), O(m) space where m is the total types of unique candy < (n/2) 
          counter = 0
          candyTypesEaten = {}
          remaining = len(candyType) / 2
          for current_candy in candyType:
            if current_candy not in candyTypesEaten and remaining != 0:
              remaining -= 1
              counter += 1
              candyTypesEaten[current_candy] = 0
          return len(candyTypesEaten)
    
    def distributeCandies(self, candyType: List[int]) -> int:
        # O(n) time and O(m) space but a tiny bit faster than my solution above
        # Count the number of unique candies by creating a set with
        # candyType, and then taking its length.
        unique_candies = len(set(candyType))
        # And find the answer in the same way as before.
        return min(unique_candies, len(candyType) // 2)
