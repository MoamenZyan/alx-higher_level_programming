#include "lists.h"

/**
 * *insert_node - inserting node
 * @head: head of the node
 * @number: value of node
 * Return: address of node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *current = *head;
	int i = 0;

	if (new == NULL)
		return (NULL);

	new->n = number;
	while (current->next != NULL && current->next->n < number)
	{
		++i;
		current = current->next;
	}

	if (i == 0)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	else if (i > 0 && current == NULL)
	{
		new->next = NULL;
		current->next = new;
		return (new);
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
