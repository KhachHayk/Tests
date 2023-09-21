import pytest
from db.tasks import *


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors, 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)']
    ]
)
def test_top_name(mentors_, expected):
    result = top_uniq_name(mentors)
    assert result == expected


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors, "На курсах 'Python-разработчик с нуля' и 'Java-разработчик с нуля' преподают: Антон, Евгений, Максим\n"
                "На курсах 'Python-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Александр, Евгений, Елена, Кирилл, Максим, Олег, Роман\n"
                "На курсах 'Python-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Александр, Евгений\n"
                "На курсах 'Java-разработчик с нуля' и 'Fullstack-разработчик на Python' преподают: Денис, Евгений, Максим\n"
                "На курсах 'Java-разработчик с нуля' и 'Frontend-разработчик с нуля' преподают: Денис, Евгений\n"
                "На курсах 'Fullstack-разработчик на Python' и 'Frontend-разработчик с нуля' преподают: Александр, Алена, Владимир, Денис, Евгений, Эдгар\n"]
    ]
)

def test_super_names(mentors_, expected):
    res = intersection_name_course(mentors)
    assert res == expected


@pytest.mark.parametrize(
    'mentors_, expected', [
        [mentors, 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, '
                  'Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, '
                  'Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, '
                  'Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий']
    ]
)
def test_unique_name(mentors_, expected):
    res = uniq_name(mentors_)
    assert res == expected