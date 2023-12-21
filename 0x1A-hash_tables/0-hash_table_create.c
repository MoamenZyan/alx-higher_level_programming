#include "hash_tables.h"

/**
 * *hash_table_create - function to create hash table
 * @size: size of the array
 * Return: returns pointer to the table if there is error return NULL
*/

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table = malloc(sizeof(hash_table_t));

	if (table == NULL)
		return (NULL);
	table->array = calloc(size, sizeof(hash_node_t));
	if (table->array == NULL)
		return (NULL);

	table->size = size;
	return (table);
}
