#ifndef LISTS_H
#define LISTS_H
struct ListNode
{
	int data;
	struct ListNode* next;
};
typedef struct ListNode listint;
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint *list);

#endif
