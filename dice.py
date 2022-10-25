from random import randint


def dice_code(code: str):
    y = 0
    z = 0
    add_sub = ""
    code_l = code.lower()
    index_d = code_l.find("d")
    if index_d < 0:
        return "Please Give a dice code in format [xDy+z]: "
    else:
        if code_l.index("d") == 0:
            x = 1
        else:
            x = int(code_l[0:index_d])

        if (code_l.find("+") < 0) and (code_l.find("-") < 0):
            z = 0
            y = int(code_l[index_d+1::])
            add_sub = ""
            if not (int(code_l[index_d+1::]) in [3, 4, 6, 8, 10, 12, 20, 100]):
                return "Please choose dice in format: D3, D4, D6, D8, D10, D12, D20, D100."
        elif code_l.find("+") >= 0:
            index_p = code_l.index("+")
            z = int(code_l[index_p+1::])
            y = int(code_l[index_d+1:index_p])
            add_sub = "+"
            if not (int(code_l[index_d+1:index_p]) in [3, 4, 6, 8, 10, 12, 20, 100]):
                return "Please choose dice in format: D3, D4, D6, D8, D10, D12, D20, D100."
        elif code_l.find("-") >= 0:
            index_m = code_l.index("-")
            z = int(code_l[index_m+1::])
            y = int(code_l[index_d+1:index_m])
            add_sub = "-"
            if not (int(code_l[index_d+1:index_m]) in [3, 4, 6, 8, 10, 12, 20, 100]):
                return "Please choose dice in format: D3, D4, D6, D8, D10, D12, D20, D100."

    what_we_have = {
        "x": x,
        "y": y,
        "z": z,
        "m": add_sub
    }
    return what_we_have


def calculate_result(user_choice: dict):
    if user_choice.get("z") == 0:
        return user_choice.get("x") * randint(1, user_choice.get("y")+1)
    elif user_choice.get("z") != 0:
        if user_choice.get("m") == "+":
            return user_choice.get("x") * randint(1, user_choice.get("y")+1) + user_choice.get("z")
        if user_choice.get("m") == "-":
            return user_choice.get("x") * randint(1, user_choice.get("y")+1) + user_choice.get("z")


cos_tam = input("Give a dice code [xDy+z]: ")
print(dice_code(cos_tam))
print(calculate_result(dice_code(cos_tam)))
