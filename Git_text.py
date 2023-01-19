# Runs on python 3.10 and above as match case is not present in any other python version

file_name = input("Kindly enter player's name: ")
with open(f"{file_name}.txt", "w") as file:
    pass


def coin_flip_probability():
    flag = True
    while flag:
        coin_flip = input("Throw the coin and enter head or tail here: ? ").lower() + "\n"
        match coin_flip:
            case "head\n":
                # read the files
                with open(f"{file_name}.txt", "r") as files:
                    result = files.readlines()

                result.append(coin_flip)

                # write the data into files
                with open(f"{file_name}.txt", 'w') as files:
                    files.writelines(result)

                # print(f"this is result: {result}")
                probality_head = (result.count('head\n') / len(result)) * 100
                print(f"Heads: {probality_head}%")

            case "tail\n":
                # Read the files
                with open(f"{file_name}.txt", "r") as files:
                    result = files.readlines()

                result.append(coin_flip)

                # write the data into files
                with open(f"{file_name}.txt", "w") as files:
                    files.writelines(result)

                # print(f"this is result: {result}")
                probality_head = (result.count('head\n') / len(result)) * 100
                print(f"Heads: {probality_head}%")

            case "exit\n":
                flag = False
                print("Thank you for using our program now you are exit!!!")

            case _:
                print("Kindly enter a valid input!!!")


# coin_flip_probability()

