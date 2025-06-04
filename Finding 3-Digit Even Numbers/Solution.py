from collections import Counter


class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = Counter(digits)
        result = []

        def backtrack(path):
            if len(path) == 3:
                r = int(''.join(str(p) for p in path))
                if r % 2 == 0 and r not in result:
                    result.append(r)
                return
            for ch in counter:
                if counter[ch] > 0:
                    if len(path) == 0 and ch == 0:
                        continue
                    counter[ch] -= 1
                    path.append(ch)
                    backtrack(path)
                    path.pop()
                    counter[ch] += 1

        backtrack([])
        return sorted(result)

new_object = Solution()
digits = [2,1,3,0]
print(new_object.findEvenNumbers(digits))