from unittest import TestCase

from daily_solutions.year_2021.day_16 import (
    Year2021Day16Solution,
    extract_operator,
    extract_operator_15,
    extract_version_id,
    hex_to_binary,
    parse_literal,
    parse_operator,
    parse_operator_15,
)

example = []


class Day16SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.solution = Year2021Day16Solution
        self.data = self.solution.format_data(example)

    def test_solve_part_1(self) -> None:
        self.assertEqual(None, self.solution.solve_part_1(self.data))

    def test_solve_part_2(self) -> None:
        self.assertEqual(None, self.solution.solve_part_2(self.data))


class Day16HelpersTestCase(TestCase):
    def test_extract_version_id(self) -> None:
        version, packet_id, packet_str = extract_version_id("110100101111111000101000")
        self.assertEqual(version, 6)
        self.assertEqual(packet_id, 4)
        self.assertEqual(packet_str, "101111111000101000")

        version, packet_id, packet_str = extract_version_id(
            "11101110000000001101010000001100100000100011000001100000"
        )
        self.assertEqual(version, 7)
        self.assertEqual(packet_id, 3)
        self.assertEqual(
            packet_str, "10000000001101010000001100100000100011000001100000"
        )

    def test_parse_literal(self) -> None:
        literal, packet_str = parse_literal("101111111000101000")
        self.assertEqual(2021, literal)
        self.assertEqual("", packet_str)

        literal, packet_str = parse_literal("1011111110001010001111")
        self.assertEqual(2021, literal)
        self.assertEqual("1111", packet_str)

    def test_parse_operator(self) -> None:
        # L = 11
        packets, packet_str = extract_operator(
            "10000000001101010000001100100000100011000001100000"
        )
        self.assertEqual(3, len(packets))
        self.assertEqual(["01010000001", "10010000010", "00110000011"], packets)
        self.assertEqual("0000", packet_str)

        # L = 15
        packets, packet_str = extract_operator(
            "00000000000110111101000101001010010001001000000000"
        )
        self.assertEqual(2, len(packets))
        self.assertEqual(["01010010001", "0001001000000000"], packets)

    def test_parse_operator_15(self) -> None:

        # L = 15
        packet, remainder = parse_operator_15(
            "0000000000110111101000101001010010001001000000000"
        )
        self.assertEqual("0000000000011011110100010100101001000100100", packet)
        self.assertEqual("0000000", remainder)

    def test_integration(self) -> None:
        binary_str = hex_to_binary("8A004A801A8002F478")

        # Should be '0b100010100000000001001010100000000001101010000000000000101111010001111000'

        # Outer packet - operator with version 4
        version, packet_id, packet_str = extract_version_id(binary_str)
        self.assertEqual(4, version)
        self.assertEqual(2, packet_id)
        self.assertEqual(
            "100000000001001010100000000001101010000000000000101111010001111000",
            packet_str,
        )
        packet_str, remainder = parse_operator(packet_str)
        self.assertEqual("100000000001001010100000000001101", packet_str)
        self.assertEqual("010000000000000101111010001111000", remainder)

        # Next packet - operator with version 1
        version, packet_id, packet_str = extract_version_id(remainder)
        self.assertEqual(1, version)
        packet_str, remainder = parse_operator(packet_str)
        self.assertEqual("", packet_str)

        # Next packet - operator with version 5
        version, packet_id, packet_str = extract_version_id(remainder)
        self.assertEqual(5, version)
        packet_str, remainder = parse_operator(packet_str)
        self.assertEqual("", packet_str)

        # Final packet - literal with version 6
        version, packet_id, packet_str = extract_version_id(remainder)
        self.assertEqual(6, version)
        packet_str, remainder = parse_operator(packet_str)
        self.assertEqual("", packet_str)
