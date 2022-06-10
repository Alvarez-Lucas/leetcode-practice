from typing import List
from pprint import pprint
from collections import defaultdict


class Solution:
    # Initial
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in strs:
            key = str(sorted(word))
            results[key].append(word)
        return [val for val in reversed(results.values())]

    # other solution, count the numbers of each letter,
    # map it to a list where the index is the asci value (adjusted)
    # use that as the key


def main():
    test = Solution()
    print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
