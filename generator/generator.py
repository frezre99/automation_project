from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')

def generator_person():
    yield Person(
        full_name= f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address(),
    )