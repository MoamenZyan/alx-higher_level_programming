#include "hash_tables.h"

/**
 * hash_table_print - printing hash table
 * @ht: hash table
 * Return: Void
*/

void hash_table_print(const hash_table_t *ht)
{
	unsigned long int i;
	int first_element = 1;

	printf("{");
	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i] != NULL)
		{
			if (!first_element)
				printf(", ");
			printf("'%s': '%s'", ht->array[i]->key, ht->array[i]->value);
			first_element = 0;
		}
	}
	printf("}\n");
}
