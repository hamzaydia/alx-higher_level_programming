#include "lists.h"

/**
  * check_cycle - Check if a singly list has a loop
  * @list: listint_t
  * Return: int
  */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	slow = list;
	fast = list;
	do
	{
		if (fast == NULL || fast->next == NULL)
			return (0);
		slow = slow->next;
		fast = fast->next->next;
	} while (slow != fast);
	return(1);
}
