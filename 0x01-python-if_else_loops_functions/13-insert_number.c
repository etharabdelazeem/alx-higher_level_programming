#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head of the list
 * @number: the number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (h == NULL || h->n >= number)
	{
		new->next = h;
		*head = new;
		return (new);
	}
	while (h && h->next && h->next->n < number)
		h = h->next;

	new->next = h->next;
	h->next = new;

	return (new);
}
