class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda x:x[1])
        prev_end=float('-inf')
        removal=0
        for start,end in intervals:
            if start>=prev_end:
                prev_end=end
            else:
                removal+=1
        return removal

   