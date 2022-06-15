import llists


def reverse_sublist(l: llists.ListNode, s: int, f: int) -> llists.ListNode:
    static_head = sublist_iter = llists.ListNode(0, l)

    # move sublist head to s steps
    for _ in range(1, s):
        sublist_iter = sublist_iter.next

    # reverse the sublist
    # Concept: 3 pointers: head, iter and swap. at each iteration, cut 'swap' out and paste it in front of 'head'.
    iter = sublist_iter.next
    for _ in range(f - s):
        swap = iter.next
        # cut it out
        iter.next = swap.next
        # move to front
        swap.next = sublist_iter.next
        sublist_iter.next = swap

    return static_head.next


# TEST CASES
a = llists.create_from_list([i for i in range(10)])
llists.print_chain(reverse_sublist(a, 2, 8))


# LEARNING QUESTINOS
