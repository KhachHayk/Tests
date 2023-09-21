courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
def uniq_name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
      name = mentor.split()[0]
      all_names_list.append(name)
    uniq_names = list(set(all_names_list))
    all_names_sorted = sorted(uniq_names)
    return (f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}')


def top_uniq_name(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)
    all_names_list = []
    for mentor in all_list:
      name = mentor.split()[0]
      all_names_list.append(name)
    # unique_names = list(set(all_names_list))
    popular = []
    for name in all_names_list:
      popular.append((name, all_names_list.count(name)))

    popular = list(set(popular))
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[0 : 3]
    top_str = []
    for name, count in top_3:
       top_str.append(name + ': ' + str(count))
    return (f'{" раз(а), ".join(top_str)} раз(а)')


def intersection_name_course(mentors):
    mentors_names = []
    for m in mentors:
      course_names = []
      for name in m:
        course_names.append(name.split()[0])
      mentors_names.append(course_names)
    pairs = []
    list_mentors = []
    for id1 in range(len(mentors_names)):
      for id2 in range(len(mentors_names)):
        if id1 == id2:
          continue
        intersection_set = set(mentors_names[id1]).intersection(set(mentors_names[id2]))
        if len(intersection_set) > 0:
          pair = {courses[id1], courses[id2]}
          if pair not in pairs:
                pairs.append(pair)
                all_names_sorted = sorted(intersection_set)
                list_mentors.append(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(str(i) for i in all_names_sorted)}\n")
    return f'{list_mentors[0]}{list_mentors[1]}{list_mentors[2]}{list_mentors[3]}{list_mentors[4]}{list_mentors[5]}'