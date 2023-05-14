#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
*is_palindrome - ...
*head: ...
*Return: ...
*/
int is_palindrome(listint_t **head)
{
listint_t *tmp = *head;
listint_t *front, *rear;
int j = 0, i, c = 0;
if (*head == NULL || (*head)->next == NULL)
{
return (1);
}
while (tmp != NULL)
{
tmp = tmp->next;
c++;
}
while (j != c / 2)
{
front = rear = *head;
for (i = 0; i < j; i++)
{
front = front->next;
}
for (i = 0; i < c - (j + 1); i++)
{
rear = rear->next;
}
if (front->n != rear->n)
{
return (0);
}
else
{
j++;
}
}
return (1);
}
