import random

marks = ['spades', 'diamonds', 'hearts', 'clubs']
card_english = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# 파일 입출력
def load():
    try:
        f = open("money.dat", 'r')
        return int(f.readline())
    except FileNotFoundError:
        f = open("money.dat", 'w')
        f.write('100000')
        return 100000


def write(money):
    f = open("money.dat", 'w')
    f.write(money)
    f.close()

# 결과에 따라 보유금액 저장
def set_money(now, betting, num):
    # lose : 0
    if num == 0:
        write(str(now - betting))
        return now - betting
    # win : 1
    elif num == 1:
        write(str(now + betting))
        return now + betting
    # Black jack : 3
    elif num == 3:
        write(str(int(now + (1.5 * betting))))
        return int(now + (betting * 1.5))
    else:
        return now


# 플레이어와 딜러에게 카드 두장씩 지급, 카드뭉치에서 카드 제거
def twocard(card):
    cardList = []
    for i in range(2):
        cardList.append(card.pop(0))
    return cardList


# 카드뭉치에서 새로운 카드 받기
def cardappend(cardlist, card):
    cardlist.append(card.pop(0))


# end 버튼 클릭 이벤트, Lose: 0 Win: 1 Draw 2
def fight(player_result, dealer_result):
    if player_result == dealer_result:
        return 2
    elif player_result < dealer_result:
        return 0
    elif player_result > dealer_result:
        return 1

# burst인지 확인
def burst(result):
    if result > 21:
        return True

# 결과 리턴
def get_fight_text(num):
    if num == 0:
        return "Lose"
    elif num == 1:
        return "Win"
    elif num == 3:
        return "Black Jack!!"
    else:
        return "Draw"

# 카드 뭉치 생성
def set_card():
    return random.sample(range(52), 17)

# 카드패의 합 계산
def count(card):
    result = 0
    cnt = 0
    for data in card:
        if data % 13 >= 10:
            result += 10
        else:
            result += data % 13 + 1
            # if data == A
            if data % 13 == 0:
                cnt += 1

    for _ in range(cnt):
        # A : 1 or 11
        if result + 10 <= 21:
            result += 10
        else:
            break

    return result

# 카드패를 문자열로 변환
def intToString_card(card):
    card_list = []
    for data in card:
        cardsuit = marks[data//13]
        cardnumber = card_english[data % 13]
        card = str(cardsuit) + str(cardnumber)
        card_list.append(card)
    return card_list

# stay시 dealer card에 카드패 추가
def dealer_algo(result, who, card):
    while result <= 16:
        cardappend(who, card)
        if count(who) > 16:
            break
