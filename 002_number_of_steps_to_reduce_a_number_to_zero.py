class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            # num = func_i(num)
            if mod(num,2)==0:
                num = num/2
            elif mod(num,2)==1:
                num = num - 1 
            step += 1
        return step

    # def func_i(self, num_i):
    #     if mod(num_i,2)==0:
    #         return num_i/2
    #     elif mod(num_i,2) == 1:
    #         return num_i-1
