puzzleinput = "59777373021222668798567802133413782890274127408951008331683345339720122013163879481781852674593848286028433137581106040070180511336025315315369547131580038526194150218831127263644386363628622199185841104247623145887820143701071873153011065972442452025467973447978624444986367369085768018787980626750934504101482547056919570684842729787289242525006400060674651940042434098846610282467529145541099887483212980780487291529289272553959088376601234595002785156490486989001949079476624795253075315137318482050376680864528864825100553140541159684922903401852101186028076448661695003394491692419964366860565639600430440581147085634507417621986668549233797848"
#puzzleinput = "12345678"

data = [[int(i),0] for i in puzzleinput]

def FFT(data):
    result = []
    pattern=[0,1,0,-1]
    patternIndex = 0
    patternCounter = 0
    
    for patternBase,value in enumerate(data, start=1):        
        patternCounter = 0
        patternIndex = 0
        for d in data:
            patternCounter += 1
            if patternCounter == patternBase:
                patternCounter = 0
                patternIndex += 1
                patternIndex %= len(pattern)
            d[1] = pattern[patternIndex]
        #print(data, end=" = ")
        res = sum(map(lambda a: a[0]*a[1],data))
        res = abs(res)%10
        #print(res)
        result.append([res,0])

    return result

for i in range(100):
    data = FFT(data)
    
print("".join(map(lambda a: str(a[0]), data)))
        