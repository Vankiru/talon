from talon import Module

mod = Module()
mod.tag("code_operators", desc="Operators commands")

@mod.action_class
class Actions:
    def code_operator_plus():
        """+"""

    def code_operator_minus():
        """-"""

    def code_operator_multiplication():
        """*"""

    def code_operator_division():
        """/"""

    def code_operator_modulus():
        """%"""

    def code_operator_exponent():
        """**"""

    def code_operator_set_to():
        """="""

    def code_operator_set_variable_to(name: str):
        """="""

    def code_operator_plus_equal():
        """+="""

    def code_operator_minus_equal():
        """-="""

    def code_operator_multi_equal():
        """*="""

    def code_operator_divide_equal():
        """/="""

    def code_operator_modulus_equal():
        """%="""

    def code_operator_power_equal():
        """**="""

    def code_operator_equal():
        """=="""

    def code_operator_not_equal():
        """!="""

    def code_operator_great():
        """>"""

    def code_operator_less():
        """<"""

    def code_operator_great_equal():
        """>="""

    def code_operator_less_equal():
        """<="""

    def code_operator_and():
        """and"""

    def code_operator_or():
        """or"""

    def code_operator_not():
        """not"""

    def code_operator_index():
        """[]"""

    def code_operator_bit_and():
        """&"""

    def code_operator_bit_or():
        """|"""

    def code_operator_bit_xor():
        """^"""

    def code_operator_bit_not():
        """~"""

    def code_operator_bit_left_shift():
        """>>"""

    def code_operator_bit_right_shift():
        """<<"""
