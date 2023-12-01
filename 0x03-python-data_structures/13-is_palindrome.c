#include "lists.h"

/**
 * listint_len - calculate the length of a linked list
 * @head: pointer to head of list
 * Return: number of nodes
 */

int listint_len(listint_t *head)
{
	int i = 0;
	listint_t *current = head;

	while (current != NULL)
	{
		i++;
		current = current->next;
	}
	return (i);
}

/**
 * is_palindrome - checks if linked list is a palindrome or not
 * @head: pointer to head of list
 * Return: 1 if palindrome 0 if not
 */

int is_palindrome(listint_t **head)
{
	int len = listint_len(*head), arr[len], i = 0, j = len;
	listint_t *current = *head;

	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0; i < len; i++)
	{
		j--;
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
