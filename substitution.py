import time
start = time.time()

percent = .05

ucifer = {}

f = open('word_freq_cleaned.txt', 'r')
words = f.read().split('\n')
words = words[:int(len(words)*percent)]
f.close()

abc = 'abcdefghijklmnopqrstuvwxyz'

connections = []


def baseSub(text):
    output = ''
    tempSub = {' ':' '}
    abcIndex = 0
    for letter in text:
        if letter in tempSub:
            output += tempSub[letter]
        else:
            output += abc[abcIndex]
            tempSub[letter] = abc[abcIndex]
            abcIndex += 1
    return output


def getMatchingWords(base):
    output = []
    for word in words:
        if baseSub(word) == base:
            output.append(word)
    return output



text = baseSub('fhttxhm mywhv gth ytv sng ys y sxlh ik irddvgextp sbh pagcha ytv sbh whphsyidh lyt ytv sbh irscbha rtsxd gthm cbhhom irathv nxsb sbh mxdhts xlfrsysxgt gj fyamxlgtk sbys mrcb cdgmh vhydxtp xlfdxhv').split(' ')


wordPos = [] # word posibilities

for word in text:
    wordPos.append(getMatchingWords(baseSub(word)))

per = -1
pairs = {}
def loop(string, per, depth=0):
    if depth == 1:
        per += 1
        print(round(per/len(connections[1])*100), '%')
    if baseSub(string[1:]) == ' '.join(text[:depth]):
        if depth == len(text):
            disp = string[1:].split(' ')
            p = [pairs]
            for a in range(len(disp)):
                try:
                    p[a][disp[a]]
                except:
                    p[a][disp[a]] = {}
                p.append(p[a][disp[a]])
        else:
            for a in connections[depth][string.split(' ')[-1:][0]]:
                try:
                    per = loop(string+' '+a, per, depth+1)
                except KeyError:pass
    return per

connections.append({'':[]})
for a in wordPos[0]:
    connections[0][''].append(a)
for i in range(len(text)-1):
    print(round((i+1)/len(text)*100, 1), '%')
    connections.append({})
    for a in wordPos[i]:
        connections[i+1][a] = []
        for b in wordPos[i+1]:
            if baseSub(' '.join(text[i:2+i]))==baseSub(' '.join([a,b])):
                connections[i+1][a].append(b)
        if connections[i+1][a] == []:
            del connections[i+1][a]
print('100.0 %')
print('conections made')
loop('', per)
end = time.time()
print('\nDone in', end - start)

try:
    p = [pairs]
    while True:
        out = ''
        for a in range(len(text)):
            for b in p[a]:
                print(b)
            i = input(' >')
            try:
                p.append(p[a][i])
                out += i+' '
            except:
                print(i, 'is not in the list')
        print(out)
        input('')
except:
    print(pairs)
