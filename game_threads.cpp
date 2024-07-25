#include <iostream>
#include <windows.h>
using namespace std;


volatile int comand_1 = 100 + rand() % 150, comand_2 = 100 + rand() % 150;


void thread()
{
	srand(time(NULL));
	int kk = 0;

	for (;;)
	{


		comand_1 += 1 + rand() % 15;
		comand_2 += 1 + rand() % 15;

		Sleep(500);

		comand_2 -= 1 + rand() % 30;

		comand_1 -= 1 + rand() % 30;



	}



}


int main()
{
	setlocale(LC_ALL, "ru");

	HANDLE hThread_one, hThread_two;
	DWORD IDThread_one, IDThread_two;


	hThread_one = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)thread, NULL, 0, &IDThread_one);
	hThread_two = CreateThread(NULL, 0, (LPTHREAD_START_ROUTINE)thread, NULL, 0, &IDThread_two);

	if ((hThread_one == NULL) or (hThread_two == NULL))
		GetLastError();



	for (;;)
	{
		cout << "Армия 1-ой команды: " << comand_1 << endl;
		cout << "Армия 2-ой команды: " << comand_2 << endl;

		cout << endl << endl;

		Sleep(500);

		if (((comand_1 == 0) and (comand_2 == 0)) or ((comand_1 < 0) and (comand_2 < 0)) or ((comand_1 == 0) and comand_2 < 0)) or ((comand_2 == 0) and (comand_1 < 0))
		{
			cout << "Ничья" << endl;
			cout << "В живых у 1-ой команды не осталось бойцов: " << 0 << endl;
			cout << "В живых у 2-ой команды не осталось бойцов: " << 0 << endl;
			break;
		}

		if ((comand_1 == 0) or (comand_1 < 0))
		{
			if ((comand_1 < 0) and (comand_2 > 0))
			{  
				comand_1 = 0;
			}

			if ((comand_1 > 0) and (comand_2 < 0))
			{
				comand_2 = 0;
			}

			cout << "Вторая команда выиграла!!!" << endl;
			cout << "В живых у 1-ой команды не осталось бойцов: " << comand_1 << endl;
			cout << "В живых у 2-ой команды осталось бойцов: " << comand_2 << endl;
			break;
		}



		if ((comand_2 == 0) or (comand_2 < 0))
		{

			if ((comand_1 < 0) and (comand_2 > 0))
			{
				comand_1 = 0;
			}

			if ((comand_1 > 0) and (comand_2 < 0))
			{
				comand_2 = 0;
			}

			cout << "Первая команда выиграла!!!" << endl;
			cout << "В живых у 1-ой команды осталось бойцов: " << comand_1 << endl;
			cout << "В живых у 2-ой команды не осталось бойцов: " << comand_2 << endl;
			break;
		}




	}

	TerminateThread(hThread_one, 0);
	CloseHandle(hThread_one);

	TerminateThread(hThread_two, 0);
	CloseHandle(hThread_two);

}

























