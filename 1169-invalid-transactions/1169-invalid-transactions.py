class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        t_map = defaultdict(lambda : defaultdict(set))
        for t in transactions:
            name, time, amount, city = t.split(',')
            t_map[int(time)][name].add(city)
        
        for t in transactions:
            name, time, amount, city = t.split(',')
            time = int(time)
            if int(amount) > 1000:
                invalid.append(t)
                continue
                
            for t_range in range(max(0, time-60), time+61):
                if t_map[t_range][name] - set([city]):
                    invalid.append(t)
                    break
        
        return invalid