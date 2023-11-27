#ifndef LISTS_H
#define LISTS_H
struct ListNode
{
	int data;
	struct ListNode* next;
};
typedef struct ListNode listint;

int check_cycle(listint *list);

#endif
