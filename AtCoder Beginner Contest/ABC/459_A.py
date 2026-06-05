S = "HelloWorld"
X = int(input())


result = str()

for i, s in enumerate(S):
    if i != X-1:
        result = result + s        

print(result)