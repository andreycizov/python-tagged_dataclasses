import unittest
from typing import Optional, Any

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
        class Union(TaggedUnion[A]):
            first: Optional[AB] = None
            second: Optional[AC] = None

        val_a = Union.from_value(AB())
        val_b = Union.from_value(AC())
        if val_b.kind == AC:
            print(val_b)
            pass

        with self.assertRaisesRegex(ValueError, 'not a member of tagged union'):
            Union.from_value(A())

        with self.assertRaisesRegex(ValueError, 'tagged union only supports one value at a time'):
            Union(
                first=AB(),
                second=AC(),
            )

    def test_init(self):
        with self.assertRaisesRegex(TypeError, 'unsupported fields found'):
            @dataclass
            class Union(TaggedUnion[Any]):
                first: int = 0

