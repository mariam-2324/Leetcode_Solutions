class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = [[0]]
        result = []
        target = len(graph) - 1

        while q:
            temp = q.pop(0)

            if temp[-1] == target:
                result.append(temp)
            else:
                for neighbours in graph[temp[-1]]:
                    q.append (temp + [neighbours])

        return result
        
        
        
        
        
        
        
        
        # q = [[0]]
        # result = []
        # target = len(graph) - 1

        # while q:
        #     temp = q.pop(0)
        #     if temp[-1] == target:
        #         result.append(temp)

        #     else:
        #         for neighbours in graph[temp[-1]]:
        #             q.append(temp + [neighbours])
        # return result
                
