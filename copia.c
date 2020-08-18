#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// Variables globales

int gruposTotal, elementosTotal, casoP, cantidadElementos;
float FP_Global, TgFinal, Qi, potenciaActivaTotal, potenciaAparente, Qf, Qc;

// Variables para suma de almacenamiento dinamico

float varSumaPotenciaActivaElemental, varSumaQiElemental, varSumaPotenciaActivaGrupal, varSumaQiGrupal;

// Variables resultados Globales

float valorPotenciaActivaGlobal, valorPotenciaAparenteGlobal, valorQiGlobal, valorQfGlobal, valorQcGlobal;

int main(){

	printf("\nCuantos grupos hay?\n");
	scanf("%d", & gruposTotal);

	printf("\nIngrese FP para compensamiento global\n");
	scanf("%f", & FP_Global);

	printf("\nIngresar Tg final correspondiente al FP\n");
	scanf("%f", & TgFinal);

	printf("\nCuantos elementos tiene en total la instalacion?\n");
	scanf("%d", & cantidadElementos);

    // Arrays
	float valorDeQcElemental[gruposTotal];
	float valorDeQfElemental[gruposTotal];
	float valorAparenteElemental[gruposTotal];
	float sumaDeQiElemental[gruposTotal];
	float sumapotenciaActivaElemental[gruposTotal];
	float QiElemental[cantidadElementos][gruposTotal];
	float QfElemental[cantidadElementos][gruposTotal];
	float QcElemental[cantidadElementos][gruposTotal];
	float potenciaActivaTotalElemental[cantidadElementos][gruposTotal];
	float potenciaAparenteElemental[cantidadElementos][gruposTotal];

	int i, j;

	for (i = 0; i <= gruposTotal - 1; ++i){

		printf("\nCuantos elementos hay en el grupos numero %d\n", i + 1);
		scanf("%d", & elementosTotal);

		varSumaPotenciaActivaElemental = 0;
		varSumaQiElemental = 0;

		for (j = 0; j <= elementosTotal - 1; ++j){

			printf("\nElemento numero %d", j + 1);

			printf("\n\nTenes la potencia activa o la aparente?\nNumero 1 para W\nNumero 2 para VA\n");
			scanf("%d", & casoP);

			if (casoP == 1){

				int cantidad;
				float potenciaActiva, FP_Elemento;

				printf("\nIngrese la potencia activa\n");
				scanf("%f", & potenciaActiva);

				printf("\nIngrese el valor de FP\n");
				scanf("%f", & FP_Elemento);

				printf("\nIngrese la cantidad\n");
				scanf("%d", & cantidad);

				potenciaActivaTotal = potenciaActiva * cantidad;
				potenciaAparente = potenciaActivaTotal / FP_Elemento;
				Qi = sqrt((potenciaAparente * potenciaAparente) - (potenciaActivaTotal * potenciaActivaTotal));
				Qf = potenciaActivaTotal * TgFinal;
				Qc = Qi - Qf;

				printf("\nWT = %f", potenciaActivaTotal);
				printf("\nVA = %f", potenciaAparente);
				printf("\nQi = %f", Qi);
				printf("\nQf = %f", Qf);
				printf("\nQc = %f\n", Qc);

			}

			else if (casoP == 2){

				float FP_Elemento;

				printf("\nIngrese la potencia aparente\n");
				scanf("%f", & potenciaAparente);

				printf("\nIngrese el valor de FP\n");
				scanf("%f", & FP_Elemento);

				potenciaActivaTotal = potenciaAparente * FP_Elemento;
				Qi = sqrt((potenciaAparente * potenciaAparente) - (potenciaActivaTotal * potenciaActivaTotal));
				Qf = potenciaActivaTotal * TgFinal;
				Qc = Qi - Qf;

				printf("\nW = %f", potenciaActivaTotal);
				printf("\nQi = %f", Qi);
				printf("\nQf = %f", Qf);
				printf("\nQc = %f\n", Qc);

			}

			potenciaActivaTotalElemental[j][i] = potenciaActivaTotal;
			potenciaAparenteElemental[j][i] = potenciaAparente;
			QiElemental[j][i] = Qi;
			QfElemental[j][i] = Qf;
			QcElemental[j][i] = Qc;

			varSumaPotenciaActivaElemental = varSumaPotenciaActivaElemental + potenciaActivaTotalElemental[j][i];
			varSumaQiElemental = varSumaQiElemental + QiElemental[j][i];

		}

		sumapotenciaActivaElemental[i] = varSumaPotenciaActivaElemental;
		sumaDeQiElemental[i] = varSumaQiElemental;
		valorAparenteElemental[i] = sqrt(pow(sumapotenciaActivaElemental[i], 2) + pow(sumaDeQiElemental[i], 2));
		valorDeQfElemental[i] = sumapotenciaActivaElemental[i] * TgFinal;
		valorDeQcElemental[i] = sumaDeQiElemental[i] - valorDeQfElemental[i];

		printf("\n\nLos valores grupales son: ");
		printf("\nWT: %f", sumapotenciaActivaElemental[i]);
		printf("\nS: %f", valorAparenteElemental[i]);
		printf("\nQi: %f", sumaDeQiElemental[i]);
		printf("\nQf: %f", valorDeQfElemental[i]);
		printf("\nQc: %f\n\n", valorDeQcElemental[i]);

		varSumaPotenciaActivaGrupal = varSumaPotenciaActivaGrupal + sumapotenciaActivaElemental[i];
		varSumaQiGrupal = varSumaQiGrupal + sumaDeQiElemental[i];

	}

	valorPotenciaActivaGlobal = varSumaPotenciaActivaGrupal;
	valorQiGlobal = varSumaQiGrupal;
	valorPotenciaAparenteGlobal = sqrt(pow(valorPotenciaActivaGlobal, 2) + pow(valorQiGlobal, 2));
	valorQfGlobal = valorPotenciaActivaGlobal * TgFinal;
	valorQcGlobal = valorQiGlobal - valorQfGlobal;

	printf("\n\nLos valores gloabales son: ");
	printf("\nWT: %f", valorPotenciaActivaGlobal);
	printf("\nS: %f", valorPotenciaAparenteGlobal);
	printf("\nQi: %f", valorQiGlobal);
	printf("\nQf: %f", valorQfGlobal);
	printf("\nQc: %f\n\n", valorQcGlobal);

	
	// Esta parte crea la opcion de poder crear una hoja de excel a partir de los datos
	char hoja_de_excel;

	printf("¿Quiere crear una hoja de excel con los datos?\n\nSi: y\nNo: n");
	scanf("%c", &hoja_de_excel);

	if (hoja_de_excel == "y")
	{
		FILE *file = fopen("Hoja_de_datos.csv", "a");
	}

	else
	{
		 
	}

}

