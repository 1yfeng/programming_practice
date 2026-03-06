import pytest

from src.algorithm.common import *

def test_binary_tree():
    # trav_seq = "124##7##3##"
    trav_seq = "1234##5##6##78###"
    # trav_seq = "abdg##hj#k#l###e##c#fim##n#opq###"
    t = BinaryTree.from_traversal_sequence(trav_seq)
    print()
    t.print_tree()
    print()
    # t.pre_order_iter()

    print()
    # t.pre_order_iter_opt()
    print()
    t.in_order_iter()

