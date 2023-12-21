#include "hash_tables.h"

/**
 * hash_table_delete - function to delete hash table
 * @ht: hash table
 * Return: void
*/

void hash_table_delete(hash_table_t *ht)
{
	unsigned int i;

	for (i = 0; i < ht->size; i++)
	{
		hash_node_t *current = ht->array[i];

		if (current != NULL)
		{
			hash_node_t *next = current->next;

			free(current->key);
			free(current->value);
			free(current);
			current = next;
		}
	}
	free(ht->array);
	ht->array = NULL;
	ht->size = 0;
	free(ht);
}
