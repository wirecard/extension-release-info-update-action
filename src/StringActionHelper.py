import re


class StringActionHelper:

    @staticmethod
    def find_part_to_replace(string) -> str:
        """
        Returns part of the string from first digit to last digit
        :return: string
        """
        return string[StringActionHelper.find_first_digit_index_in_string(string):
                      StringActionHelper.find_last_digit_index_in_string(string)]

    @staticmethod
    def find_first_digit_index_in_string(string) -> int:
        """
        Returns index of first digit in string
        :return: int
        """
        m = re.search(r'\d', string)
        if m is not None:
            return m.start()

    @staticmethod
    def find_last_digit_index_in_string(string):
        """
        Returns negative index of last digit in string
        :return: int or Nona
        """
        m = re.search(r'\d', string[::-1])
        if m is not None:
            if m.start() == 0:
                return None
            return -m.start()
