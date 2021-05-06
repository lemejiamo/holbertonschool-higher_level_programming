#include "lists.h"
/**
* is_palindrome- verify if a list is palindrome
* @head: pointer to head of a list
* Return: 0 if failde 1 if success
*/
int is_palindrome(listint_t **head)
{
	/* declaration of vars */
	int i = 0, j = 0;
	listint_t *current = NULL, **array = NULL;

	current = *head;
	/* searching the length of a list */
	for (; current != NULL; j++)
	{
		current = current->next;
	}
	/* assingnament of memory to array */
	array = malloc((sizeof(listint_t) * (j)));
	j -= 1;
	if (array == NULL)
		return (-1);
	/* add pointers the list to array possitions */
	current = *head;
	for (i = 0; current != NULL; i++)
	{
		array[i] = current;
		current = current->next;
	}
	array[i] = NULL; /* added null to end of array */
	/* /\* test printing *\/ */
	/* for(i = 0; array[i] != NULL; i++) */
	/* { */
	/* printf("direccion of position %d %p\n", i, (void *)array[i]); */
	/* } */
	/* comparation bettewen the positions in the list */
	for (i = 0; i <= j; i++, j--)
	{
		if (array[i]->n != array[j]->n)
			return (0);
	}
return (1); /* is palindrome */

}
