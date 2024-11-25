#!/usr/bin/python3
def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes of data.
    :return: True if valid UTF-8, False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking leading bits
    mask_1_byte = 0b10000000  # 128: Checks the most significant bit
    mask_2_bytes = 0b11100000  # 224: Checks the first 3 bits
    mask_3_bytes = 0b11110000  # 240: Checks the first 4 bits
    mask_4_bytes = 0b11111000  # 248: Checks the first 5 bits
    mask_continuation = 0b11000000  # 192: Checks the first 2 bits

    for byte in data:
        # Consider only the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if byte & mask_1_byte == 0:
                # Single-byte character (1-byte)
                continue
            elif byte & mask_2_bytes == 0b11000000:
                # Two-byte character
                num_bytes = 1
            elif byte & mask_3_bytes == 0b11100000:
                # Three-byte character
                num_bytes = 2
            elif byte & mask_4_bytes == 0b11110000:
                # Four-byte character
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check continuation bytes
            if byte & mask_continuation != 0b10000000:
                return False
            num_bytes -= 1

    # If all characters are processed, num_bytes should be 0
    return num_bytes == 0
