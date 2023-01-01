from typing import Any, List, Tuple, Union

from daily_solutions.base import BaseDailySolution

"""
As you leave the cave and reach open waters, you receive a transmission from the Elves back on the ship.

The transmission was sent using the Buoyancy Interchange Transmission System (BITS), a method of packing numeric
expressions into a binary sequence. Your submarine's computer has saved the transmission in hexadecimal (your puzzle
input).

The first step of decoding the message is to convert the hexadecimal representation into binary. Each character of
hexadecimal corresponds to four bits of binary data:

0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
The BITS transmission contains a single packet at its outermost layer which itself contains many other packets. The
hexadecimal representation of this packet might encode a few extra 0 bits at the end; these are not part of the
transmission and should be ignored.

Every packet begins with a standard header: the first three bits encode the packet version, and the next three bits
encode the packet type ID. These two values are numbers; all numbers encoded in any packet are represented as binary
with the most significant bit first. For example, a version encoded as the binary sequence 100 represents the number 4.

Packets with type ID 4 represent a literal value. Literal value packets encode a single binary number. To do this, the
binary number is padded with leading zeroes until its length is a multiple of four bits, and then it is broken into
groups of four bits. Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit. These groups
of five bits immediately follow the packet header. For example, the hexadecimal string D2FE28 becomes:

110100101111111000101000
VVVTTTAAAAABBBBBCCCCC
Below each bit is a label indicating its purpose:

The three bits labeled V (110) are the packet version, 6.
The three bits labeled T (100) are the packet type ID, 4, which means the packet is a literal value.
The five bits labeled A (10111) start with a 1 (not the last group, keep reading) and contain the first four bits of the
number, 0111.
The five bits labeled B (11110) start with a 1 (not the last group, keep reading) and contain four more bits of the
number, 1110.
The five bits labeled C (00101) start with a 0 (last group, end of packet) and contain the last four bits of the number,
0101.
The three unlabeled 0 bits at the end are extra due to the hexadecimal representation and should be ignored.
So, this packet represents a literal value with binary representation 011111100101, which is 2021 in decimal.

Every other type of packet (any packet with a type ID other than 4) represent an operator that performs some calculation
on one or more sub-packets contained within. Right now, the specific operations aren't important; focus on parsing the
hierarchy of sub-packets.

An operator packet contains one or more packets. To indicate which subsequent binary data represents its sub-packets, an
operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the
length type ID:

If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the
sub-packets contained by this packet.
If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately
contained by this packet.
Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.

For example, here is an operator packet (hexadecimal string 38006F45291200) with length type ID 0 that contains two
sub-packets:

00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
The three bits labeled V (001) are the packet version, 1.
The three bits labeled T (110) are the packet type ID, 6, which means the packet is an operator.
The bit labeled I (0) is the length type ID, which indicates that the length is a 15-bit number representing the number
of bits in the sub-packets.
The 15 bits labeled L (000000000011011) contain the length of the sub-packets in bits, 27.
The 11 bits labeled A contain the first sub-packet, a literal value representing the number 10.
The 16 bits labeled B contain the second sub-packet, a literal value representing the number 20.
After reading 11 and 16 bits of sub-packet data, the total length indicated in L (27) is reached, and so parsing of this
packet stops.

As another example, here is an operator packet (hexadecimal string EE00D40C823060) with length type ID 1 that contains
three sub-packets:


VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
The three bits labeled V (111) are the packet version, 7.
The three bits labeled T (011) are the packet type ID, 3, which means the packet is an operator.
The bit labeled I (1) is the length type ID, which indicates that the length is a 11-bit number representing the number
of sub-packets.
The 11 bits labeled L (00000000011) contain the number of sub-packets, 3.
The 11 bits labeled A contain the first sub-packet, a literal value representing the number 1.
The 11 bits labeled B contain the second sub-packet, a literal value representing the number 2.
The 11 bits labeled C contain the third sub-packet, a literal value representing the number 3.
After reading 3 complete sub-packets, the number of sub-packets indicated in L (3) is reached, and so parsing of this
packet stops.

For now, parse the hierarchy of the packets throughout the transmission and add up all of the version numbers.

Here are a few more examples of hexadecimal-encoded transmissions:

8A004A801A8002F478 represents an operator packet (version 4) which contains an operator packet (version 1) which
contains an operator packet (version 5) which contains a literal value (version 6); this packet has a version sum of 16.
620080001611562C8802118E34 represents an operator packet (version 3) which contains two sub-packets; each sub-packet is
an operator packet that contains two literal values. This packet has a version sum of 12.
C0015000016115A2E0802F182340 has the same structure as the previous example, but the outermost packet uses a different
length type ID. This packet has a version sum of 23.
A0016C880162017C3686B18A3D4780 is an operator packet that contains an operator packet that contains an operator packet
that contains five literal values; it has a version sum of 31.
Decode the structure of your hexadecimal-encoded BITS transmission; what do you get if you add up the version numbers in
all packets?
"""


def hex_to_binary(hex_str: str) -> str:
    return str(bin(int(hex_str, 16)))[2:]


def sum_versions(packet_str: str) -> int:
    version_sum = 0
    version, packet_id, packet_str = extract_version_id(packet_str)
    version_sum += version

    if version == 4:
        return version_sum + sum_versions_literal(packet_str)
    else:
        return version_sum + sum_versions_operator(packet_str)


def sum_versions_literal(packet_str: str) -> int:
    version, packet_id, packet_str = extract_version_id(packet_str)
    _, packet_str = parse_literal(packet_str)
    return version + sum_versions(packet_str)


def sum_versions_operator(packet_str: str) -> int:
    if packet_str[0] == "0":
        return sum_versions_operator_15(packet_str[1:])
    return sum_versions_operator_11(packet_str[1:])


def sum_versions_operator_15(packet_str: str) -> int:
    pass


def sum_versions_operator_11(packet_str: str) -> int:
    pass


def get_next_packet(packet_str: str) -> Tuple[str, str]:
    version, packet_id, packet_str = extract_version_id(packet_str)
    if version == 4:
        return parse_literal(packet_str)
    else:
        return parse_operator(packet_str)


def extract_packet(packet_str: str) -> Tuple[Union[int, str], str]:
    version, packet_id, packet_str = extract_version_id(packet_str)
    print(version)
    if version == 4:
        return evaluate_literal(packet_str)
    return parse_operator(packet_str)


def parse_literal(packet_str: str) -> Tuple[str, str]:
    literal = ""
    group = packet_str[0:5]
    packet_str = packet_str[5:]

    while group[0] == "1":
        literal += group
        group = packet_str[0:5]
        packet_str = packet_str[5:]
    # Add the final group
    literal += group

    # Figure out how many 0s to truncate
    # This packet originally included a header
    packet_bits = len(literal) + 6
    remainder = 4 - int(packet_bits % 4)
    return literal, packet_str[remainder:]


def extract_version_id(packet_str: str) -> Tuple[int, int, str]:
    # Every packet begins with a standard header: the first three bits encode the packet version, and the next three
    # bits encode the packet type ID.
    version = int(packet_str[0:3], 2)
    packet_id = int(packet_str[3:6], 2)
    packet_str = packet_str[6:]

    return version, packet_id, packet_str


def evaluate_literal(packet_str: str) -> Tuple[int, str]:
    literal = ""
    group = packet_str[0:5]
    packet_str = packet_str[5:]

    while group[0] == "1":
        literal += group[1:]
        group = packet_str[0:5]
        packet_str = packet_str[5:]
    # Add the final group
    literal += group[1:]

    # Figure out how many 0s to truncate
    # Each group in the literal originally included 5 bits
    literal_bits = (len(literal) / 4) * 5
    packet_bits = literal_bits + 6
    remainder = 4 - int(packet_bits % 4)
    return int(literal, 2), packet_str[remainder:]


def parse_operator(packet_str: str) -> Tuple[str, str]:
    if packet_str[0] == "0":
        return parse_operator_15(packet_str[1:])
    return parse_operator_11(packet_str[1:])


def parse_operator_15(packet_str: str) -> Tuple[str, str]:
    subpacket_length = int(packet_str[:15], 2)
    packet_length = subpacket_length + 15

    return "0" + packet_str[:packet_length], packet_str[packet_length:]


def parse_operator_11(packet_str: str) -> Tuple[str, str]:
    num_packets = int(packet_str[:11], 2)

    # Strip off the trailing 0s and return the rest of the packet string
    # This packet contains num_packets packets of length 11, plus one length bit, plus a 6-bit header
    packet_bits = 11 * (num_packets + 1) + 6 + 1
    remainder = 4 - int(packet_bits % 4)
    total_length = packet_bits + remainder

    return "1" + packet_str[:total_length], packet_str[total_length:]


def extract_operator(packet_str: str) -> Tuple[List[str], str]:
    if packet_str[0] == 0:
        return extract_operator_15(packet_str[1:])
    return extract_operator_11(packet_str[1:])


def extract_operator_11(packet_str: str) -> Tuple[List[str], str]:
    num_packets = int(packet_str[:11], 2)
    packet_str = packet_str[11:]

    packets = []
    while len(packets) != num_packets:
        packets.append(packet_str[:11])
        packet_str = packet_str[11:]

    # Strip off the trailing 0s and return the rest of the packet string
    # This packet contains num_packets packets of length length, plus one length bit, plus a 6-bit header
    packet_bits = 11 * (num_packets + 1) + 6 + 1
    remainder = 4 - int(packet_bits % 4)

    return packets, packet_str[remainder:]


def extract_operator_15(packet_str: str) -> Tuple[List[str], str]:
    length = int(packet_str[:15], 2)
    packet_str = packet_str[15:]
    print(length)

    packets = []
    packet_length = 0
    while packet_length < length:
        _, remainder = extract_packet(packet_str)
        this_packet = len(packet_str) - len(remainder)
        packet_length += this_packet
        packets.append(packet_str[:this_packet])
        packet_str = packet_str[this_packet:]

    return packets, packet_str


class Year2021Day16Solution(BaseDailySolution):
    YEAR = 2021
    DAY = 16

    @classmethod
    def format_data(cls, input_data: List[str]) -> str:
        return hex_to_binary(input_data[0].strip())

    @classmethod
    def solve_part_1(cls, input_data: Any) -> int:
        return 0

    @classmethod
    def solve_part_2(cls, input_data: Any) -> int:
        pass
