class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        bal = sum_gas = sum_cost = index = 0
        if len(gas) == 0 or len(gas) != len(cost):
            return -1
        
        for i in range(len(cost)):
            sum_gas += gas[i]
            sum_cost += cost[i]
            bal += gas[i] - cost[i]
            if bal < 0:
                index = i+1
                bal = 0
        
        if (sum_gas < sum_cost) or index >= len(gas):
            return -1
        
        return index