
#include "lists.h"

/**
 * insert_node - inserts  num to sorted linked list.
 * @head:head node
 * @number: number stored in new node
 * Return: returns ptr to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *old = *head, *new = NULL;

	if (*head == NULL || number <= current->n)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (number <= current->n)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			new->n = number;
			old->next = new;
			new->next = current;
			return (new);
		}
		old = current;
		current = current->next;
	}
	new = add_nodeint_end(&old, number);
	return (new);
}
