#include <stdio.h>
#include <stdlib.h>

// Global variables
int number_of_groups;
int number_of_elements;

float fp_final;
float tg_final;


// Function declaration
void show_name(void);
void ask_for_data(void);

int main(void)
{
    show_name();

    printf("\nIngrese los siguientes datos:\n");

    printf("\nCantidad de grupos: ");
    scanf("%d", &number_of_groups);

    printf("\nCantidad de elementos: ");
    scanf("%d", &number_of_elements);

    printf("\nIngrese el fp: ");
    scanf("%f", &fp_final);

    printf("\nIngrese el tg: ");
    scanf("%f", &tg_final);

    ask_for_data();
}

void show_name(void)
{
    printf("\n");

    printf("   /| |   | |'''  |   | |'''  '''|''' |'''|\n");
    printf("  / | |   | |  __ |   | |___     |    |   |\n");
    printf(" /__| |   | |   | |   |     |    |    |   |\n");
    printf("/   | |___| |___| |___|  ___|    |    |___|\n");

    printf("\n");

    printf("|'''| |'''  |'''|    /| |    \n");
    printf("|   | |___  | __|   / | |    \n");
    printf("|   |     | |      /__| |    \n");
    printf("|___|  ___| |     /   | |____\n\n");

}

void ask_for_data(void)
{
    for (int i = 0; i < number_of_groups; i++)
    {
        printf("Grupo %d", i + 1);
        printf("\nCantidad de elementos en este grupo:");
        
    }
    
}
