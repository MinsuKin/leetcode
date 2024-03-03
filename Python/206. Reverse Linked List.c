#include <stdlib.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head)
{
    int size;
    int *list;
    struct ListNode* tmp = head;
    struct ListNode* res = head;
    
    list = malloc(sizeof(int) * 5001);
    size = 0;
    while (head != NULL)
    {
        list[size] = head->val;
        head = head->next;
        size++;
    }
    size--;
    while (tmp != NULL)
    {
        tmp->val = list[size];
        tmp = tmp->next;
        size--;
    }
    // free(list);
    return res;
}

// // recursive
// struct ListNode* recurse(struct ListNode* prev, struct ListNode* curr)
// {
//     if (curr == NULL)
//         return prev;

//     // save new next node
//     struct ListNode* newNext = curr->next;  

//     // reverse
//     curr->next = prev;

//     // reverse reset of the list
//     return recurse(curr, newNext);
// }

// struct ListNode* reverseList(struct ListNode* head)
// {
//     return recurse(NULL, head);
// }