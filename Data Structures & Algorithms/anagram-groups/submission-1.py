class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # intiazlize dict - default dict

        for i in strs: # loop through orginal array
            count = [0] * 26 # inital arr of 26 due to a-z

            for j in i: # second loop through each charcter in each str
                count[ord(j) - ord("a")] += 1 # count of each characters using the ascii values in order to
                                              # find pos, += 1 due to arr starting at 0  

            res[tuple(count)].append(i)   

        return list(res.values())