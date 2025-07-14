garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail rock gravel gravel gravel gravel'


def rake_garden(garden:str):
    correct = ['gravel','rock']

    if garden == '':
        return None

    splited_garden = garden.split()
    correct_garden = ""

    for item_index in range(len(splited_garden)-1):
        if splited_garden[item_index] in correct:
            correct_garden += splited_garden[item_index]
        else:
            correct_garden += correct[0]
        correct_garden += " "

    return correct_garden[0:-1]


print(rake_garden(garden))