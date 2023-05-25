#49. Group Anagrams - Medium - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsortlist = []
        strdict = {}
        returnlist = []
        for str in strs:
            strsort = ''.join(sorted(str))
            strsortlist.append(strsort)
        
        for i, str in enumerate(strsortlist):
            if str not in strdict:
                strdict[str] = []
            strdict[str].append(i)
        
        for idxlist in strdict.values():
            tmplist = []
            for i in idxlist:
                tmplist.append(strs[i])
            returnlist.append(tmplist)
        return returnlist