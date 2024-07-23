import requests

def location(ip: str):
    response = requests.get(f'http://ip-api.com/json/{ip}?language=ru')
    if response.status_code == 404:
        print("Ошибка")
    result = response.json()
    if result["status"] == "fail":
        return main("Введите корректный ip адрес")

    record = []

    for key, value in result.items():
        record.append(value)
        print(f"[{key.title()}]: {value}")

    return tuple(record)


def main(start: str):
    print(start)
    ip = input("IP address: ")
    try:
        new_data = location(ip)
    except ValueError:
        print("hi")



if __name__ == "__main__":
    main("Введи IP Адрес")








