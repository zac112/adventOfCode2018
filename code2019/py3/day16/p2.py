
puzzleinput = "59777373021222668798567802133413782890274127408951008331683345339720122013163879481781852674593848286028433137581106040070180511336025315315369547131580038526194150218831127263644386363628622199185841104247623145887820143701071873153011065972442452025467973447978624444986367369085768018787980626750934504101482547056919570684842729787289242525006400060674651940042434098846610282467529145541099887483212980780487291529289272553959088376601234595002785156490486989001949079476624795253075315137318482050376680864528864825100553140541159684922903401852101186028076448661695003394491692419964366860565639600430440581147085634507417621986668549233797848"
puzzleinput = puzzleinput*10000
#puzzleinput="12345678"

#data = [[int(i),0] for i in puzzleinput]
data = [int(i) for i in puzzleinput]
newData = list(data)

offset = int(puzzleinput[:7])

def FFT(data, newData, offset):
    s = sum(data[offset:])    
    index = offset
    for v in data[offset:]:
        newData[index] = abs(s)%10
        s -= v
        index += 1
        
    return newData
 
for i in range(100):
    print("FFT phase",i)    
    data = FFT(data, newData, offset)

#print(data)   
print("".join(map(lambda a: str(a), data))[offset:offset+8])
        
