def game_score(n, cards):
    sereja_score, dima_score = 0, 0
    left, right = 0, n - 1
    turn = 0

    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1

        if turn == 0:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card

        turn ^= 1  # Toggle between 0 and 1 using XOR

    return sereja_score, dima_score


n = int(input())
cards = list(map(int, input().split()))
sereja, dima = game_score(n, cards)


print(sereja, dima)
