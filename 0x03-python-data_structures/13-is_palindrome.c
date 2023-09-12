#include "lists.h"

/**
 * reverse - reverses the second half of the list
 * @h_r: head of the second half
 * Return: no return
 */

void reverse(listint_t **h_r)
{
	listint_t *prev;
	listint_t *curr;
	listint_t *nxt;

	prev = NULL;
	curr = *h_r;

	while (curr != NULL)
	{
		nxt = curr->next;
		curr->next = prev;
		prev = curr;
		curr = nxt;
	}

	*h_r = prev;
}


/**
 * compare - compares each int of the list
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp1->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}

	return (0);
}


/**
 * is_palindrome - function in C that checks if a singly linked list
 * is a palindrome
 * @head: ptr to head
 * Return:returns 0 if it is not a palindrome
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *fast, *prev_s, *slow;
	listint_t *scn_half, *middle;
	int tmp;

	slow = fast = prev_s = *head;
	middle = NULL;
	tmp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_s = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}

		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		tmp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_s->next = middle;
			middle->next = scn_half;
		}
		else
		{
			prev_s->next = scn_half;
		}
	}

	return (tmp);
}
