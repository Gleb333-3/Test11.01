given_list  = [120,543, 666]

def functuan(lisst):
        answer_list = []
        for number in lisst:
                hours = number // 3600
                minutes = number // 60
                seconds = number - (hours * 3600 + minutes * 60)

                answer_list.extend([str(f"{hours}: {minutes}: {seconds}")])
        return answer_list


print(functuan(given_list))