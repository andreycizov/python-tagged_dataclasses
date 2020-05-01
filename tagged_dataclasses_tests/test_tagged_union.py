import unittest
from typing import Optional

from dataclasses import dataclass

from tagged_dataclasses import TaggedUnion


class TestTaggedUnion(unittest.TestCase):
    def test_simple(self):
        class A:
            pass

        @dataclass
        class AB(A):
            pass

        @dataclass
        class AC(A):
            pass

        @dataclass
        class Mutable(TaggedUnion[A]):
            first: Optional[AB] = None
            second: Optional[AC] = None

        val_a = Mutable.from_value(AB())
        val_b = Mutable.from_value(AC())
        if val_b.kind == AC:
            print(val_b)
            pass

        with self.assertRaisesRegexp(ValueError, 'not a member of tagged union'):
            Mutable.from_value(A())
