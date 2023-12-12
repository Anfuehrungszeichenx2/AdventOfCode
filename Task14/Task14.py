from dataclasses import dataclass
import operator

alphabet = 'AKQT98765432J'


@dataclass
class Hand:
    hand: str
    value: int

    cards: str

def isBigger(hand1,hand2):
    for i in range(len(hand1.cards)):
        indexH1 = alphabet.find(hand1.cards[i])
        indexH2 = alphabet.find(hand2.cards[i])
        if indexH2 == indexH1:
            continue
        if indexH1 < indexH2:
            return True
        elif indexH2 < indexH1:
            return False
def sortRank(hands):
    sorted = []
    if len(hands)==0:
        return hands
    if len(hands) == 1:
        return hands
    sorted.append(hands[0])
    for i in range(1,len(hands)):
        inserted = False
        for j in range(len(sorted)):
            if isBigger(hands[i],sorted[j]):
               # print(hands[i].cards + ' > ' + sorted[j].cards)
                continue
            else:
                #print(hands[i].cards + ' < ' + sorted[j].cards)
                sorted.insert(j,hands[i])
                inserted = True
                break
        if inserted == False:
            sorted.append(hands[i])
    return sorted


if __name__ == "__main__":
    file = open('Task14.input', mode='r')
    lines = file.read().splitlines()

    values = []
    hands = [[], [], [], [], [], [], []]
    for line in lines:
        cards, value = line.split()
        hand = Hand('', int(value), cards)
        h1 = Hand('',1,'Q2QQQ')
        h2 = Hand('',1,'QTTTT')

        max = 0
        rank = ''
        char = ''
        mix = []
        js = cards.count('J')
        sortedCards = sorted(cards.replace("J",""))

        for card in sortedCards:
            if card == char:
                continue
            mix.append(str(sortedCards.count(card)))
            char = card
        mix.sort(reverse=1)
        if len(mix) == 0:
            mix = ['0']
        lol = int(mix[0])+js
        mix[0] = str(lol)
        if (len(mix) == 5):
            hand.hand = '1k'
            hands[6].append(hand)
        elif len(mix) == 4:
            hand.hand = '1p'
            hands[5].append(hand)
        elif '3' in mix and '2' in mix:
            hand.hand = 'fh'
            hands[2].append(hand)
        elif mix.count('2') == 2:
            hand.hand = '2p'
            hands[4].append(hand)
        elif mix.count('3') == 1:
            hand.hand = '3k'
            hands[3].append(hand)
        elif mix.count('4') == 1:
            hand.hand = '4k'
            hands[1].append(hand)
        elif mix.count('5') == 1:
            hand.hand = '5k'
            hands[0].append(hand)
    out = 0
    counter = 1
    hands.reverse()
    for i in hands:

        sorted =  sortRank(i)
      #  print(sorted)
        for s in sorted:
            out += s.value * counter
            print(s.cards,': ' ,s.value , '*' , counter )
            counter +=1
   # print(out)





    l = 2
