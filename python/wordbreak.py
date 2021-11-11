def wordBreak(self, s: str, wordDict: List[str]) -> bool:
	wordDict = set(wordDict)

	l = len(s)

	dp = [False]*l
	dp[0] = s[0] in wordDict

	for i in range(1, l):
		for j in range(0, i+1):

			if j!=i:
				if dp[j] and s[j+1:i+1] in wordDict:
					dp[i] = True
			else:
				if s[:j+1] in wordDict:
					dp[i] = True
	return dp[l-1]