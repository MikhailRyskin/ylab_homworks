offices = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]

# формирование структуры (списка списков), которая содержит расстояния от
# каждого офиса до всех остальных офисов
all_distances = []
for start_index, start_point in enumerate(offices):
    from_office_distances = []
    for finish_index, finish_point in enumerate(offices):
        if start_index == finish_index:
            distance = 0
        elif finish_index < start_index:
            distance = all_distances[finish_index][start_index]
        else:
            distance = (abs(finish_point[0] - start_point[0]) ** 2
                        + abs(finish_point[1] - start_point[1]) ** 2) ** 0.5
        from_office_distances.append(distance)
    all_distances.append(from_office_distances)

# определение кратчайшего маршрута
routes = []
current_rout_number = 0
min_route_distance = 1000000
min_route_number = 0
ind_1 = 0
for ind_2 in range(1, 5):
    for ind_3 in range(1, 5):
        for ind_4 in range(1, 5):
            for ind_5 in range(1, 5):
                if ind_2 not in (ind_3, ind_4, ind_5) and ind_3 not in (ind_4, ind_5) and ind_4 != ind_5:
                    current_route = [ind_1, ind_2, ind_3, ind_4, ind_5, ind_1]
                    routes.append(current_route)
                    current_distance = all_distances[ind_1][ind_2] + all_distances[ind_2][ind_3] \
                                       + all_distances[ind_3][ind_4] + all_distances[ind_4][ind_5] \
                                       + all_distances[ind_5][ind_1]
                    if current_distance < min_route_distance:
                        min_route_distance = current_distance
                        min_route_number = current_rout_number
                    current_rout_number += 1

# вывод результата в соответствии с требованиями
min_route_list = routes[min_route_number]
accumulated_distance = [0]
distance_count = 0
for ind in range(5):
    distance_count += all_distances[min_route_list[ind]][min_route_list[ind + 1]]
    accumulated_distance.append(distance_count)
print(offices[0], end='')
for ind in range(1, 6):
    print(' ->', offices[min_route_list[ind]], accumulated_distance[ind], end='')
print(' =', min_route_distance)
