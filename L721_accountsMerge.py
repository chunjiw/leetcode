# 721. Accounts Merge
# DescriptionHintsSubmissionsDiscussSolution
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Example 1:
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Note:

# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # build graph
        email2acc = dict()
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email2acc:
                    email2acc[email].append(i)
                else:
                    email2acc[email] = [i]
        graph = [[] for _ in accounts]
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                graph[i] += email2acc[email]
        # traverse graph
        visited = set()
        res = []
        for i in range(len(graph)):
            if i in visited:
                continue
            acc = [accounts[i][0], []]
            # breath first search
            level = [i]
            while level:
                node = level.pop(0)
                if node in visited:
                    continue
                visited.add(node)
                acc[1] += accounts[node][1:]
                for child in graph[node]:
                    level.append(child)
            acc[1] = sorted(list(set(acc[1])))
            res.append([acc[0]] + acc[1])
        return res


