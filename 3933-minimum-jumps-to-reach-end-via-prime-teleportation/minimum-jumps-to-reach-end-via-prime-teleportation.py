class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        def is_prime(x):
            if x < 2: return False
            if x == 2: return True
            if x % 2 == 0: return False
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0: return False
            return True

        def prime_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors

        #primes that acutaly appear as vals in nums
        primes_in_nums = {v for v in nums if is_prime(v)}

        #for each prime p collect all idx j where num[j]%p is 0
        prime_to_indices = defaultdict(list)
        for i, v in enumerate(nums):
            for p in prime_factors(v):
                if p in primes_in_nums:
                    prime_to_indices[p].append(i)

        dist = [-1] * n
        dist[0] = 0
        queue = deque([0])
        processed_primes = set()   #avoid expanding the same group

        while queue:
            idx = queue.popleft()
            if idx == n - 1:
                return dist[idx]

            #adjacent steps
            for nxt in (idx - 1, idx + 1):
                if 0 <= nxt < n and dist[nxt] == -1:
                    dist[nxt] = dist[idx] + 1
                    queue.append(nxt)

            #prime tp
            p = nums[idx]
            if is_prime(p) and p not in processed_primes:
                processed_primes.add(p)
                for j in prime_to_indices[p]:
                    if dist[j] == -1:
                        dist[j] = dist[idx] + 1
                        queue.append(j)

        return dist[n - 1]