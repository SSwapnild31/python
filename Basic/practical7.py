class card:
    suit=()
    value=()
def __init__(self,string):
    set.suit=string[1]
    self.value=string[0]
def __it__(self.rank() < other.rank()):
    return self.value() < other.rank()
def __eq__(self.other):
    return self.rank()==other.rank()
class Hand:
    cards=[]
    rank=0
    def __init__(self,string):
        self.card=[card(x) for x in string]
if _ name : == '__main__':
    f=open('input.txt')
    while True:
        line=f.readline()
        if line=='':
            break
        hand1=Hand(line[0:14].split())
        hand2=Hand(line[15:].split())
        if hand2<hand1:
            print("Black wins")
        elif hand1<hand2:
            print("white wins")
        else:
            print("Tie")
