
def lengthOfLongestSubstring( s):
    max_length = 0
    x = 0
    y = 0
    counts = {}

    for i in range(len(s)):
        if s[y] not in counts:
            counts[s[y]] = 0
        counts[s[y]] += 1

        for j in counts:
            if counts[j] > 1:
                counts[s[x]] -= 1
                x += 1

       
        if y-x+1 > max_length:
            max_length = y-x+1
        y += 1
        
    return max_length
        

print(lengthOfLongestSubstring("pwwkew"))

