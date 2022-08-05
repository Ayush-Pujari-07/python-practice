def students_grade():
    student_score = {
        "Harry": 81,
        "Ron": 78,
        "Hermioney": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grade = {}

    for key in student_score:
        if student_score[key] > 90:
            student_grade[key] = 'Outstanding'
        elif student_score[key] > 80:
            student_grade[key] = 'Exceeds Expectations'
        elif student_score[key] > 70:
            student_grade[key] = 'Acceptable'
        else:
            student_grade[key] = 'Fail'

    print(student_grade)


def travel_logs():
    capital = {
        "France": "paris",
        "Germany": "Berlin"
    }

    travel_log = [
        {
            "country": "France",
            "city": ["Paris", "Little", "Digjon"],
            "total_Visit": 10
        },
        {
            "country": "Germany",
            "city": ["Berlin", "Humberg", "frankfut"],
            "total_visit": 5
        }
    ]

    def add_new_country(country_name, total_visit_time, city_names):
        new_dictionary = {"country": country_name, "city": city_names, "total_visits": total_visit_time}
        travel_log.append(new_dictionary)
        return travel_log

    add_new_country("Russia", 2, ["Moscow", "saint Petersburg", "Siberia"])

    print(travel_log)


# *--------------------Project---------------------*#
# Declaring the function for auction

def start_auction():
    counter = True
    # Gets the list of bidder
    bidder_list = []
    print("Welcome to the secret auction program.")
    # keep the list of  bid amount
    bid_amount_list = []

    def blind_auction(bidder_lists):
        for lists in bidder_lists:
            bid_amount_list.append(lists["bid_amount"])
        index = bid_amount_list.index(max(bid_amount_list))
        print(f"The Winner is {bidder_lists[index]['name']} with a bid of ${(bidder_lists[index]['bid_amount'])}.")

    while counter:

        # Details of the bidders

        name_of_bidder = input("What is your name?: ")
        bid_amount = int(input("what's your bid?: $"))

        # Creating dictionary
        bid_dictionary = {
            "name": name_of_bidder,
            "bid_amount": bid_amount,
        }

        # Creating a list of bidders
        bidder_list.append(bid_dictionary)
        flag = input("Are there any other bidders? Type 'yes' of 'no'.\n")
        if flag == "no":
            counter = False
            # print(bidder_list)
            blind_auction(bidder_list)
        else:
            continue


print(start_auction())
