class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_counter = {}
        
        for winner, loser in matches:
            if winner not in loss_counter:
                loss_counter[winner] = 0
            loss_counter[loser] = loss_counter.get(loser, 0) + 1
            
        noLoss = []
        oneLoss = []
        
        for player, losses in loss_counter.items():
            if losses == 0:
                noLoss.append(player)
            elif losses == 1:
                oneLoss.append(player)
                
        noLoss.sort() #beast 
        oneLoss.sort()
        
        return [noLoss, oneLoss]