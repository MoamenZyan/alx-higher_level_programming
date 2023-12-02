#include "lists.h"

/**
 * is_palindrome - checks if linked list is a palindrome or not
 * @head: pointer to head of list
 * Return: 1 if palindrome 0 if not
 */

int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j;
	listint_t *current = *head;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}
	int arr[len];

	current = *head;
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	j = len;
	for (i = 0; i < len; i++)
	{
		j--;
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
