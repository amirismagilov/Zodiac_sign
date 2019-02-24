def zodiac_sign_Calculation(mouth, day):
    """
    >>> zodiac_sign_Calculation(3,22)
    'овен'

    >>> zodiac_sign_Calculation(1, 21)
    'водолей'
    """
    if mouth > 12 and day > 31:
        return print("Введите корретные значение")

    if mouth == 3 and day >= 21 or mouth == 4 and day <= 21:
        sign = "овен"

    if mouth == 4 and day >= 22 or mouth == 5 and day <= 22:
        sign = "телец"

    if mouth == 5 and day >= 23 or mouth == 6 and day <= 21:
        sign = "близнецы"

    if mouth == 6 and day >= 22 or mouth == 7 and day <= 21:
        sign = "рак"

    if mouth == 7 and day >= 22 or mouth == 8 and day <= 21:
        sign = "лев"

    if mouth == 8 and day >= 22 or mouth == 9 and day <= 22:
        sign = "дева"

    if mouth == 9 and day >= 23 or mouth == 10 and day <= 25:
        sign = "весы"

    if mouth == 10 and day >= 26 or mouth == 11 and day <= 23:
        sign = "скорпион"

    if mouth == 11 and day >= 24 or mouth == 12 and day <= 21:
        sign = "стрелец"

    if mouth == 12 and day >= 22 or mouth == 1 and day <= 19:
        sign = "козерог"

    if mouth == 1 and day >= 20 or mouth == 2 and day <= 18:
        sign = "водолей"

    if mouth == 2 and day >= 19 or mouth == 3 and day <= 20:
        sign = "рак"

    return sign