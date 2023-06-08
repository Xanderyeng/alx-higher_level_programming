#include "lists.h"

/**
 * check_cycle - check if list is loop.
 * @list: list to check.
 * Return: 0 if not cycle or 1 if cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp, *tmp2;

	tmp = tmp2 = list;
	while (list && tmp && tmp2 && tmp->next && tmp2->next)
	{
		tmp = tmp->next;
		tmp2 = tmp2->next->next;
		if (tmp2 == NULL)
			return (0);
		if (tmp2->next == tmp)
			return (1);
	}
	return (0);
}
