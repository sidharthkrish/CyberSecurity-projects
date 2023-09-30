#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void randomPasswordGeneration(int N)
{
    int i = 0;
  
    int randomizer = 0;

//seeding with the current time
    srand((unsigned int)(time(NULL)));

    char numbers[] = "0123456789";
    char letter[] = "abcdefghijklmnoqprstuvwyzx";
    char LETTER[] = "ABCDEFGHIJKLMNOQPRSTUYWVZX";
    char symbols[] = "!@#$^&*?()<>{}[]";
    char password[N];

    randomizer = rand() % 4;

//generating the password <3
    for (i = 0; i < N; i++) {
  
        if (randomizer == 1) {
            password[i] = numbers[rand() % 10];
            randomizer = rand() % 4;
            printf("%c", password[i]);
        }
        else if (randomizer == 2) {
            password[i] = symbols[rand() % 16];
            randomizer = rand() % 4;
            printf("%c", password[i]);
        }
        else if (randomizer == 3) {
            password[i] = LETTER[rand() % 26];
            randomizer = rand() % 4;
            printf("%c", password[i]);
        }
        else {
            password[i] = letter[rand() % 26];
            randomizer = rand() % 4;
            printf("%c", password[i]);
        }
    }
}
  
// this is the main function of the program
int main()
{
    int N;
    printf("enter the length of the password");
    scanf("%d",&N);
    randomPasswordGeneration(N);
    return 0;
}