class Solution:
    # O(N) time, O(N) space
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer += ["FizzBuzz"]
            elif i % 3 == 0:
                answer += ["Fizz"]
            elif i % 5 == 0:
                answer += ["Buzz"]
            else:
                answer += [str(i)]
        return answer
