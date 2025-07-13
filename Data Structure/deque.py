import collections

DoubleEnded = collections.deque(["Mon","Tue","Wed"])

DoubleEnded.append("Thu")
print(DoubleEnded)

DoubleEnded.appendleft("Sun")
print(DoubleEnded)

DoubleEnded.pop()
print(DoubleEnded)

DoubleEnded.popleft()
print(DoubleEnded)