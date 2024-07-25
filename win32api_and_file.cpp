#define _CRT_SECURE_NO_WARNINGS
#define CreateWindow
#include <iostream>
#include <windows.h>
#include <fstream>

using namespace std;




class User
{
public:
	bool proverka(string l, string p)
	{
		if (l == login && p == password)
		{
			cout << "Вход разрешен" << endl;
			return true;
		}
		else
		{
			cout << "Вход запрещен" << endl;
			return false;
		}
	
	}

private:
	string login = "YOUR_LOGIN";
	string password = "YOUR_PASSWORD";
};



int main()
{
	setlocale(LC_ALL, "ru");
	User user;
	string l, p;

	cout << "Введите логин -> ";
	cin >> l;

	cout << "Введите пароль -> ";
	cin >> p;


	if (user.proverka(l, p) == true)
	{
		DWORD size = 255;
		char name[255];
		GetComputerNameA(name, &size);
		cout << "Имя вашего компьютера -> " << name << endl;

		time_t loct = time(NULL);
		tm timee = *localtime(&loct);

		printf("%.2d:%.2d:%.2d", timee.tm_hour, timee.tm_min, timee.tm_sec);
		cout << endl;

		DWORD sizee = 255;
		char user_name[255];
		GetUserNameA(user_name, &sizee);
		cout << "Имя вашего пользователя -> " << user_name;


		LPWSTR DNSName = NULL;

		GetComputerNameEx(ComputerNameDnsDomain, DNSName, &size);

		cout << "Домен вашего ПК -> " << DNSName << endl;

		int count = GetSystemMetrics(SM_CMOUSEBUTTONS);


		cout << "Кол-во кнопок на вашем PC: " << count;
		ofstream file("log.txt");

		if (!file.is_open())
		{
			cout << "Произошла оишбка при записи";
			file.close();
		}
		else
		{
			file << "Имя Вашего ПК -> " << name << endl << "Локальное время: " << timee.tm_hour << ":" << timee.tm_min << ":" << timee.tm_sec << endl << "Имя пользователя -> " << user_name
				<< endl << "Домен вашего PC" << DNSName << endl << "Кол-во кнопок на вашей мыши: " << count;
			file.close();

		}


	}
	else
	{
		cout << "Выход из системы";
	}



}