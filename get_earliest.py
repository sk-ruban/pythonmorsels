def get_earliest(*dates):
    date_dict = {}
    for date in dates:
        date_dict[date] = F"{date[-4:]}{date[:2]}{date[3:5]}"
    return min(date_dict, key=date_dict.get)


get_earliest("01/27/1832", "01/27/1756")
get_earliest("02/29/1972", "12/21/1946")
get_earliest("02/24/1946", "03/21/1946")
get_earliest("06/21/1958", "06/24/1958")

