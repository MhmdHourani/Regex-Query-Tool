import re


def regex_query(regex, test_string):
    """"""
    list_tuples_indices = []
    matches = re.finditer(regex, test_string, re.MULTILINE)

    list_matches = []
    for matchNum, match in enumerate(matches, start=1):
        print("Match {matchNum} was found at {start}-{end}: {match}".format(
            matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))
        tuple_start_end_indices = match.start(), match.end()
        list_tuples_indices.append(tuple_start_end_indices)

        list_matches.append(match.group())
    return list_matches, list_tuples_indices
    # return list_matches


# regex = r"([A-Z])\w+"

# test_str = "Lorem ipsum dolor sit amet, nam no malis graecis incorrupte. Dicunt insolens sed ex, ut saepe quaerendum eam. Eum no quas tempor impetus, in per expetendis reprimique mediocritatem. Meis erant facilisi cu ius, utroque moderatius voluptatibus no nam. Pri an graecis torquatos accommodare. Quodsi everti ei qui"
# print(regex_query(regex, test_str))
