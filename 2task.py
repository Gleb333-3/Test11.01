given_list = ["right", "right","right","right","right","right","right","right"]

def finding(lisst):
    total_time = 0
    for value in lisst:
        if value == "right":
            total_time += 90
    number_circle = total_time // 360
    return  number_circle

print(finding(given_list))
