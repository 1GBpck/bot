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
			cout << "���� ��������" << endl;
			return true;
		}
		else
		{
			cout << "���� ��������" << endl;
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

	cout << "������� ����� -> ";
	cin >> l;

	cout << "������� ������ -> ";
	cin >> p;


	if (user.proverka(l, p) == true)
	{
		DWORD size = 255;
		char name[255];
		GetComputerNameA(name, &size);
		cout << "��� ������ ���������� -> " << name << endl;

		time_t loct = time(NULL);
		tm timee = *localtime(&loct);

		printf("%.2d:%.2d:%.2d", timee.tm_hour, timee.tm_min, timee.tm_sec);
		cout << endl;

		DWORD sizee = 255;
		char user_name[255];
		GetUserNameA(user_name, &sizee);
		cout << "��� ������ ������������ -> " << user_name;


		LPWSTR DNSName = NULL;

		GetComputerNameEx(ComputerNameDnsDomain, DNSName, &size);

		cout << "����� ������ �� -> " << DNSName << endl;

		int count = GetSystemMetrics(SM_CMOUSEBUTTONS);


		cout << "���-�� ������ �� ����� PC: " << count;
		ofstream file("log.txt");

		if (!file.is_open())
		{
			cout << "��������� ������ ��� ������";
			file.close();
		}
		else
		{
			file << "��� ������ �� -> " << name << endl << "��������� �����: " << timee.tm_hour << ":" << timee.tm_min << ":" << timee.tm_sec << endl << "��� ������������ -> " << user_name
				<< endl << "����� ������ PC" << DNSName << endl << "���-�� ������ �� ����� ����: " << count;
			file.close();

		}


	}
	else
	{
		cout << "����� �� �������";
	}



}