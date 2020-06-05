def find_merge_node(head_a, head_b):
    curr_a = head_a
    curr_b = head_b

    while curr_a != curr_b:
        if curr_a.next is None:
            curr_a = head_b
        else:
            curr_a = curr_a.next

        if curr_b.next is None:
            curr_b = head_a
        else:
            curr_b = curr_b.next

    curr_a.data