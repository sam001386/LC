class Solution(object):
    def letterCombinations(self, digits):
        dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []
        res = []
        def dfs(path, digits, index):
            if len(path) == len(digits):
                res.append(path)
                return 
            for index in range(index, len(digits)):
                for cur in dic[digits[index]]:
                    dfs(path + cur, digits, index + 1)
        
        dfs("", digits, 0)
        return res
