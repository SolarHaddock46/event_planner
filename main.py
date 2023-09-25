from datetime import datetime


class Event:
    def __init__(self, name, date_time, location, description):
        self.name = name
        self.date_time = datetime.strptime(date_time, "%H:%M %d-%m-%Y")
        self.location = location
        self.description = description
        self.participant_count = 0
        self.categories = []

    def add_participant(self):
        self.participant_count += 1

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.events = []

    def create_event(self, name, date_time, location, description, categories=None, participants=None):
        event = Event(name, date_time, location, description)
        if categories:
            event.categories = categories
        if participants:
            for participant in participants:
                event.add_participant()
        self.events.append(event)
        return event

    def view_events(self):
        sorted_events = sorted(self.events, key=lambda event: event.date_time)
        for event in sorted_events:
            formatted_date_time = event.date_time.strftime("%H:%M %d-%m-%Y")
            print(f"Название мероприятия: {event.name}")
            print(f"Дата и время начала: {formatted_date_time}")
            print(f"Место проведения: {event.location}")
            print(f"Описание мероприятия: {event.description}")
            print(f"Количество участников: {event.participant_count}")
            if event.categories:
                print(f"Категории: {', '.join(event.categories)}")
            print("=" * 30)

    def delete_event(self, event_name):
        for event in self.events:
            if event.name == event_name:
                self.events.remove(event)
                print(f"Мероприятие '{event_name}' было удалено.")
                break
        else:
            print(f"Мероприятие '{event_name}' не найдено.")


class UserManager:
    def __init__(self):
        self.users = []

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def find_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None


def main():
    user_manager = UserManager()

    # Создание пользователей
    user1 = user_manager.create_user("Алиса", "alice@example.com")
    user2 = user_manager.create_user("Боб", "bob@example.com")

    # Создание тестовых мероприятий
    event1 = user1.create_event("День рождения", "18:00 01-01-2024", "улица Ленина, 1", "Давайте отметим мой день рождения!",
                                categories=["Вечеринка"], participants=[user2])
    event2 = user2.create_event("Конференция", "09:00 12-11-2023", "ДК 'Компрессор'", "Конференция по вопросам "
                                                                                      "развития производства "
                                                                                      "микропроцессоров в России",
                                categories=["Технологии", "Конференция"], participants=[user1])

    # Пользовательский интерфейс
    while True:
        print("Добро пожаловать в Планировщик мероприятий!")
        print("1. Просмотреть мои мероприятия")
        print("2. Удалить мероприятие")
        print("3. Создать мероприятие")
        print("4. Создать нового пользователя")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            print("=" * 30)
            username = input("Введите имя пользователя: ")
            user = user_manager.find_user_by_username(username)
            if user:
                user.view_events()
            else:
                print("Пользователь не найден, попробуйте еще раз.")
        elif choice == "2":
            print("=" * 30)
            username = input("Введите имя пользователя: ")
            event_name = input("Введите имя мероприятия, которое вы хотите удалить: ")
            user = user_manager.find_user_by_username(username)
            if user:
                user.delete_event(event_name)
            else:
                print("Пользователь не найден, попробуйте еще раз.")
        elif choice == "3":
            print("=" * 30)
            username = input("Введите имя пользователя: ")
            user = user_manager.find_user_by_username(username)
            if user:
                name = input("Введимте название мероприятия: ")
                date_time = input("Введите дату и время начала мероприятия (ЧЧ:ММ ДД-ММ-ГГГГ): ")
                location = input("Введите место проведения мероприятия: ")
                description = input("Введите описание мероприятия: ")
                categories = input("Введите категории мероприятия (через запятую и пробел): ").split(', ')
                participants = input("Введите имена пользователей-участников (через запятую и пробел): ").split(', ')
                user.create_event(name, date_time, location, description, categories, participants)
            else:
                print("Пользователь не найден, попробуйте еще раз.")
        elif choice == "4":
            print("=" * 30)
            username = input("Введите имя нового пользователя: ")
            email = input("Введитен адрес электронной почты нового пользователя: ")
            user_manager.create_user(username, email)
            print(f"Пользователь '{username}' создан.")
        elif choice == "5":
            print("Спасибо, что воспользовались Планировщиком мероприятий!")
            break
        else:
            print("Неверный ввод. Выберите действие 1, 2, 3, 4 или 5.")


if __name__ == "__main__":
    main()
