#include "hash_tables.h"

/**
 * hash_table_set - function to add or update item in hash table
 * @ht: hash table
 * @key: item key
 * @value: item value
 * Return: return 1 if success, 0 if failure
*/

int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int hashValue = key_index((const unsigned char *)key, ht->size);
	hash_node_t *item = malloc(sizeof(hash_node_t));

	if (item == NULL)
		return (0);

	item->key = strdup(key);
	item->value = strdup(value);
	item->next = NULL;

	if (ht->array[hashValue] == NULL)
	{
		ht->array[hashValue] = item;
	}
	else
	{
		hash_node_t *current = ht->array[hashValue];

		item->next = current;
	}
	return (1);
}
