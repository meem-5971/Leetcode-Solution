class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval

        for interval in intervals:
            s, e = interval

            # Case 1: interval is completely before newInterval
            if e < start:
                result.append(interval)

            # Case 2: interval is completely after newInterval
            elif s > end:
                result.append([start, end])
                result.extend(intervals[intervals.index(interval):])
                return result

            # Case 3: intervals overlap
            else:
                start = min(start, s)
                end = max(end, e)

        # Add the merged/new interval
        result.append([start, end])

        return result
        