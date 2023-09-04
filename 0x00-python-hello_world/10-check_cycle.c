#include "lists.h"
/**
 * check_cycle - checks the cycle of a singly linked list
 * @list:list ptr
 * Return: returns 0 if there is  no cycle,
 * returns 1 otherwise
 */
int check_cycle(listint_t *list)
{
listint_t *slow_ptr;
listint_t *fast_ptr;
slow_ptr = list;
fast_ptr = list;
while (list && slow_ptr && fast_ptr && fast_ptr->next)
{
list = list->next;
slow_ptr = slow_ptr->next;
fast_ptr = fast_ptr->next->next;
if (list == fast_ptr)
{
list = slow_ptr;
slow_ptr = fast_ptr;
while (1)
{
fast_ptr = slow_ptr;
while (fast_ptr->next != list && fast_ptr->next != slow_ptr)
{
fast_ptr = fast_ptr->next;
}
if (fast_ptr->next == list)
break;

list = list->next;
}
return (1);
}
}
return (0);
}
