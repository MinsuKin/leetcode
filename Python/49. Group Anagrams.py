class Solution:

    ## Time Limit Exceeded
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     dic = {}
    #     for i in strs:
    #         dic[i] = Counter(i)
    #     res = [[strs[0]]]
    #     strs.pop(0)        
    #     for j in strs:
    #         k = 0
    #         flag = 0
    #         while (res[k]):
    #             if dic[j] == dic[res[k][0]]:
    #                 res[k].append(j)
    #                 flag = 1
    #                 break
    #             k += 1
    #             if len(res) <= k:
    #                 break
    #         if flag == 0:
    #             res.append([j])
    #     return res



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()