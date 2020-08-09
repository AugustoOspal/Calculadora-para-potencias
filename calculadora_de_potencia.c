#include <stdio.h>
#include <stdlib.h>

// Global variables
int number_of_groups;

// Function declaration
void show_name(void);
void ask_for_data(void);

int main(void)
{
    show_name();
    ask_for_data();
}

// Prints my name
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

// Ask for data and save it
void ask_for_data(void)
{
    printf("\nIngrese los siguientes datos:\n");

    for (int i = 0; i < number_of_groups; i++)
    {
        int number_of_elements_per_group;

        printf("\n\nGrupo %d", i + 1);
        printf("\nCantidad de elemetos del grupo: ");
        scanf("%d", &number_of_elements_per_group);

        for (int j = 0; j < number_of_elements_per_group; j++)
        {
            
        }
        
    }
    
}
