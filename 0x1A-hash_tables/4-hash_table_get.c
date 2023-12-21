#include "hash_tables.h"

/**
 * *hash_table_get - function to get value of item
 * @ht: hash table
 * @key: key of item
 * Return: value of item
*/

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int index = key_index((const unsigned char *)key, ht->size);

	if (ht->array[index] == NULL)
		return (NULL);

	return (ht->array[index]->value);
}
