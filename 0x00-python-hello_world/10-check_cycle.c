#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list has cycle in it
 * @list: passed head of the list
 * Return: 1 if there is cycle 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	uintptr_t ptr = (uintptr_t)current;

	current = current->next;
	while (current->next != NULL && ptr != (uintptr_t)current)
		current = current->next;

	if (current->next == NULL)
		return (0);
	return (1);
}
