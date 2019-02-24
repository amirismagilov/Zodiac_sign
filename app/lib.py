def zodiac_sign_Calculation(mouth, day):
    # """
    # >>> zodiac_sign_Calculation(3,22)
    # Овен, планета - Марс
    # """
    # if mouth > 12 and day > 31:
    #     print("Введите корретные значение")

    if mouth == 3 and day >= 21 or mouth == 4 and day <= 21:
        sign = овен

    # if mouth == 4 and day >= 22 or mouth == 5 and day <= 22:
    #     print("Телец, планета - Венера")

    return sign