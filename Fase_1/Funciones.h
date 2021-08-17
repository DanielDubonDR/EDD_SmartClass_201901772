#include <iostream>
#include <string>
#include <regex>

using namespace std;


void clear()
{
    system("cls");
}

void gotoxy(int x, int y)
{
    HANDLE hCon;
    hCon = GetStdHandle(STD_OUTPUT_HANDLE);
    COORD dwPos;
    dwPos.X = x;
    dwPos.Y = y;
    SetConsoleCursorPosition(hCon, dwPos);
}

void titulo()
{
    gotoxy(6,2); cout<<".d88888b  8888ba.88ba   .d888888   888888ba  d888888P     a88888b. dP         .d888888  .d88888b  .d88888b";
    gotoxy(6,3); cout<<"88.    '  88  `8b  `8b d8'    88   88    `8b    88       d8'   `88 88        d8'    88  88.    '  88.     '";
    gotoxy(6,4); cout<<"`Y88888b. 88   88   88 88aaaaa88a a88aaaa8P'    88       88        88        88aaaaa88a `Y88888b. `Y88888b.";
    gotoxy(6,5); cout<<"      `8b 88   88   88 88     88   88   `8b.    88       88        88        88     88        `8b       `8b";
    gotoxy(6,6); cout<<"d8'   .8P 88   88   88 88     88   88     88    88       Y8.   .88 88        88     88  d8'   .8P d8'   .8P";
    gotoxy(6,7); cout<<" Y88888P  dP   dP   dP 88     88   dP     dP    dP        Y88888P' 88888888P 88     88   Y88888P   Y88888P";

}

bool verificarEmail(string email)
{
    regex patron("^[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\\.)(com|es|org)$");
    return regex_match(email, patron);
}
