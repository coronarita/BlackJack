from innerCode import *

cards = set_card()
print('cards: ', cards)

playerCards = twocard(cards)
dealerCards = twocard(cards)

print('playerCards: ', playerCards)
print('dealerCards: ', dealerCards)

print('int to String playerCards: ', intToString_card(playerCards))
print('int to String dealerCards: ', intToString_card(dealerCards))

money = load()
print('money: ', money)
betting_money = int(input('please bet your money: '))

while True:
    print('count of playerCards...', count(playerCards))
    print('count of dealerCards...', count(dealerCards))
    if count(playerCards) == 21:
        print(get_fight_text(3))
        set_money(money,betting_money,3)
        break
    elif burst(count(playerCards)):
        print('player ' + get_fight_text(0))
        set_money(money, betting_money, 0)
        break
    else:
        result = int(input('choose Hit(1) or Stay(2): '))
        # Hit (카드 추가)
        if result == 1:
            cardappend(playerCards, cards)
            print('appended playerCards: ', playerCards)
            continue
        # Stay (승부)
        else:
            if count(dealerCards) > 17:
                print('fight!!')
            else:
                dealer_algo(count(dealerCards),dealerCards,cards)
                print('appended dealerCards: ', dealerCards)
            if count(dealerCards) == 21:
                print('dealer ' + get_fight_text(3))
                set_money(money, betting_money, 0)
                break
            elif burst(count(dealerCards)):
                print(get_fight_text(1))
                set_money(money, betting_money, 1)
                break
            else:
                res = fight(count(playerCards),count(dealerCards))
                print(get_fight_text(res))
                if res == 2:
                    set_money(money, betting_money, 2)
                elif res == 0:
                    set_money(money,betting_money,0)
                else:
                    set_money(money, betting_money, 1)
                break
money = load()
print('money: ', money)
