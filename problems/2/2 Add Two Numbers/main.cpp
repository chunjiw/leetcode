/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode *l = new ListNode();
        ListNode *head = l;
        while (l1 != nullptr || l2 != nullptr) {
            int digit = carry;
            if (l1 != nullptr) {
                digit += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                digit += l2->val;
                l2 = l2->next;
            }
            carry = digit / 10;
            digit %= 10;
            l->next = new ListNode(digit);
            l = l->next;
        }
        if (carry > 0) {
            l->next = new ListNode(carry);
        }
        return head->next;
    }
};