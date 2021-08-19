#include <iostream>
#include <string>
#include <regex>
#include <windows.h>

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
gotoxy(9,2); cout<<" $$$$$$\\  $$\\      $$\\  $$$$$$\\  $$$$$$$\\ $$$$$$$$\\  $$$$$$\\  $$\\        $$$$$$\\   $$$$$$\\   $$$$$$\\  ";
gotoxy(9,3); cout<<"$$  __$$\\ $$$\\    $$$ |$$  __$$\\ $$  __$$\\\\__$$  __|$$  __$$\\ $$ |      $$  __$$\\ $$  __$$\\ $$  __$$\\ ";
gotoxy(9,4); cout<<"$$ /  \\__|$$$$\\  $$$$ |$$ /  $$ |$$ |  $$ |  $$ |   $$ /  \\__|$$ |      $$ /  $$ |$$ /  \\__|$$ /  \\__|";
gotoxy(9,5); cout<<"\\$$$$$$\\  $$\\$$\\$$ $$ |$$$$$$$$ |$$$$$$$  |  $$ |   $$ |      $$ |      $$$$$$$$ |\\$$$$$$\\  \\$$$$$$\\  ";
gotoxy(9,6); cout<<" \\____$$\\ $$ \\$$$  $$ |$$  __$$ |$$  __$$<   $$ |   $$ |      $$ |      $$  __$$ | \\____$$\\  \\____$$\\ ";
gotoxy(9,7); cout<<"$$\\   $$ |$$ |\\$  /$$ |$$ |  $$ |$$ |  $$ |  $$ |   $$ |  $$\\ $$ |      $$ |  $$ |$$\\   $$ |$$\\   $$ |";
gotoxy(9,8); cout<<"\\$$$$$$  |$$ | \\_/ $$ |$$ |  $$ |$$ |  $$ |  $$ |   \\$$$$$$  |$$$$$$$$\\ $$ |  $$ |\\$$$$$$  |\\$$$$$$  |";
gotoxy(9,9); cout<<" \\______/ \\__|     \\__|\\__|  \\__|\\__|  \\__|  \\__|    \\______/ \\________|\\__|  \\__| \\______/  \\______/";
}

void tituloEstudiantes()
{
    gotoxy(17,4); cout<<",---.                             ,---.     |             |o          |              ";
    gotoxy(17,5); cout<<"|    ,---.,---.,---.,---.,---.    |--- ,---.|--- .   .,---|.,---.,---.|--- ,---.,---.";
    gotoxy(17,6); cout<<"|    ,---||    |   |,---||        |    `---.|    |   ||   ||,---||   ||    |---'`---.";
    gotoxy(17,7); cout<<"`---'`---^`    `---|`---^`        `---'`---'`---'`---'`---'``---^`   '`---'`---'`---'";
    gotoxy(17,8); cout<<"               `---'";
}

void tituloManual()
{
    gotoxy(26,4);   cout<<",-_/                           ,-,-,-.                   .  ";
    gotoxy(26,5);   cout<<"'  | ,-. ,-. ,-. ,-. ,-. ,-.   `,| | |   ,-. ,-. . . ,-. |  ";
    gotoxy(26,6);   cout<<".^ | | | | | |   |-' `-. | |     | ; | . ,-| | | | | ,-| |  ";
    gotoxy(26,7);   cout<<"`--' ' ' `-| '   `-' `-' `-'     '   `-' `-^ ' ' `-^ `-^ `' ";
    gotoxy(26,8);   cout<<"          ,|                                                ";
    gotoxy(26,9);   cout<<"          `'";
}

void tituloEstudiantes2()
{
                                                                                    
    gotoxy(20,4);   cout<<",------.        ,--.             ,--.,--.                  ,--.                "; 
    gotoxy(20,5);   cout<<"|  .---' ,---.,-'  '-.,--.,--. ,-|  |`--' ,--,--.,--,--, ,-'  '-. ,---.  ,---. "; 
    gotoxy(20,6);   cout<<"|  `--, (  .-''-.  .-'|  ||  |' .-. |,--.' ,-.  ||      \\'-.  .-'| .-. :(  .-' "; 
    gotoxy(20,7);   cout<<"|  `---..-'  `) |  |  '  ''  '\\ `-' ||  |\\ '-'  ||  ||  |  |  |  \\   --..-'  `)"; 
    gotoxy(20,8);   cout<<"`------'`----'  `--'   `----'  `---' `--' `--`--'`--''--'  `--'   `----'`----'";
}

void tituloIngreso()
{
    gotoxy(36,3); cout<<"_ _|                                      "; 
    gotoxy(36,4); cout<<"  |   __ \\    _` |   __|  _ \\   __|   _ \\ "; 
    gotoxy(36,5); cout<<"  |   |   |  (   |  |     __/ \\__ \\  (   |"; 
    gotoxy(36,6); cout<<"___| _|  _| \\__, | _|   \\___| ____/ \\___/ "; 
    gotoxy(36,7); cout<<"            |___/";
}

void tituloModificar()
{
    gotoxy(37,2);   cout<<"__  ___          _ _  __ _                ";
    gotoxy(37,3);   cout<<"|  \\/  |         | (_)/ _(_)               ";
    gotoxy(37,4);   cout<<"| .  . | ___   __| |_| |_ _  ___ __ _ _ __ ";
    gotoxy(37,5);   cout<<"| |\\/| |/ _ \\ / _` | |  _| |/ __/ _` | '__|";
    gotoxy(37,6);   cout<<"| |  | | (_) | (_| | | | | | (_| (_| | |   ";
    gotoxy(37,7);   cout<<"\\_|  |_/\\___/ \\__,_|_|_| |_|\\___\\__,_|_|";
}

void tituloEliminar()
{            
    gotoxy(40,4); cout<<" _____ _ _       _             ";
    gotoxy(40,5); cout<<"|   __| |_|_____|_|___ ___ ___ ";
    gotoxy(40,6); cout<<"|   __| | |     | |   | .'|  _|";
    gotoxy(40,7); cout<<"|_____|_|_|_|_|_|_|_|_|__,|_|";
}

void tituloReportes()
{
    gotoxy(37,5);  cout<<" ___   ____  ___   ___   ___  _____  ____  __  ";
    gotoxy(37,6);  cout<<"| |_) | |_  | |_) / / \\ | |_)  | |  | |_  ( (` ";
    gotoxy(37,7);  cout<<"|_| \\ |_|__ |_|   \\_\\_/ |_| \\  |_|  |_|__ _)_)";
}

bool verificarEmail(string email)
{
    regex patron("^[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\\.)(com|es|org)$");
    return regex_match(email, patron);
}

bool verificarDPI(string dpi)
{
    int cantidad = dpi.length();
    if(cantidad == 13)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool verificarCarnet(string carnet)
{
    int cantidad = carnet.length();
    if(cantidad == 9)
    {
        return true;
    }
    else
    {
        return false;
    }
}
