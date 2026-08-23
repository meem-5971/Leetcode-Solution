class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid= (high+low)//2
            if target == nums[mid]:
                ans=mid
                return ans
            if nums[mid] >= nums[low]:
                if target <nums[mid] and target >=nums[low]: 
                    high=mid-1
                else:
                    low=mid+1

            else:
                if target > nums[mid] and target <=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
            
        