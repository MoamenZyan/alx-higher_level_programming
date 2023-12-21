#include "hash_tables.h"

/**
 * key_index - this function used to get index of key
 * @key: key of the item
 * @size: size of the table
 * Return: index of the key
*/

unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int index = hash_djb2(key);

	return (index % size);
}
