#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert number in a sorted linked list 
 * @head: pointer to head of linked list
 * @number: number to insert in linkedlist
 * Return: pointer to node added 
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *new_node = NULL, *past_node = NULL;
	
	/* verify if data is valid */
	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	current = *head;
	past_node = *head;

	if (current->n < number)
		current = current->next;

	for (; current->n < number;)
	{
		past_node = past_node->next;
		current = current->next;
	}

	new_node->next = current;
	past_node->next = new_node;

	return (new_node);
}