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

	if (new == NULL)
		return (NULL);

	new->n = number;
	while (current != NULL && current->next->n < number)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
