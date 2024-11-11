def brute_force():
    from tqdm import tqdm
    import itertools, random, string, time

    startTime = int(time.time())

    alphabet = string.printable[:95]
    charLength = 5

    def generateRandPw(charLength):
        outStr = ''
        while len(outStr) < charLength:
            outStr += random.choice(alphabet)
        return outStr

    def bruteForce(pwToBrute, pwAlphabet):
        estimatedTime = int((alphabet.index(pwToBrute[0]) / len(alphabet)) * (len(alphabet) ** charLength))
        pwTuple = tuple(pwToBrute)
        charList = [[x for x in alphabet]] * len(pwToBrute)
        args = [char for char in charList]

        for combination in tqdm(itertools.product(*args), total = estimatedTime):
            if combination == pwTuple:
                return combination

    if __name__=='__main__':
        randPw = generateRandPw(charLength)
        print(f"Attempting to brute force {randPw}")
        result = bruteForce(randPw, alphabet)
        endTime = int(time.time())
        print(f"Bruteforced password {result} in {endTime - startTime} seconds")
