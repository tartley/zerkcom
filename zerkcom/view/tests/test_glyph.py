import unittest

from zerkcom.view.glyph import get_indices, get_vertices


class ShapeToGlyphTest(unittest.TestCase):

    def test_get_vertices_triangle(self):
        COLOR1 = (11, 22, 33, 44)
        self.assertEqual(
            get_vertices( [
                (COLOR1, [(1, 2), (3, 4), (5, 6)]),
            ] ),
            [
                (1, 2, 11, 22, 33, 44),
                (3, 4, 11, 22, 33, 44),
                (5, 6, 11, 22, 33, 44),
            ],
        )

    def test_get_indices_triangle(self):
        COLOR1 = (11, 22, 33, 44)
        self.assertEqual(
            get_indices( [
                (COLOR1, [(1, 2), (3, 4), (5, 6)]),
            ] ),
            [0, 1, 2]
        )

    def test_get_vertices_quad(self):
        COLOR1 = (11, 22, 33, 44)
        self.assertEqual(
            get_vertices( [
                (COLOR1, [(1, 2), (3, 4), (5, 6), (7, 8)]),
            ] ),
            [
                (1, 2, 11, 22, 33, 44),
                (3, 4, 11, 22, 33, 44),
                (5, 6, 11, 22, 33, 44),
                (7, 8, 11, 22, 33, 44),
            ],
        )

    def test_get_indices_quad(self):
        COLOR1 = (11, 22, 33, 44)
        self.assertEqual(
            get_indices( [
                (COLOR1, [(1, 2), (3, 4), (5, 6), (7, 8)]),
            ] ),
            [0, 1, 2, 0, 2, 3]
        )

