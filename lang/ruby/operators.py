from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
    def code_operator_plus():
        actions.user.vim_insert_mode(" + ", "a")

    def code_operator_minus():
        actions.user.vim_insert_mode(" - ", "a")

    def code_operator_multiplication():
        actions.user.vim_insert_mode(" * ", "a")

    def code_operator_division():
        actions.user.vim_insert_mode(" / ", "a")

    def code_operator_modulus():
        actions.user.vim_insert_mode(" % ", "a")

    def code_operator_exponent():
        actions.user.vim_insert_mode("**", "a")

    def code_operator_set_to():
        actions.user.vim_insert_mode(" = ", "a")

    def code_operator_set_variable_to(name: str):
        actions.user.vim_insert_mode(f"{name} = ", "a")

    def code_operator_plus_equal():
        actions.user.vim_insert_mode(" += ", "a")

    def code_operator_minus_equal():
        actions.user.vim_insert_mode(" -= ", "a")

    def code_operator_multi_equal():
        actions.user.vim_insert_mode(" *= ", "a")

    def code_operator_divide_equal():
        actions.user.vim_insert_mode(" /= ", "a")

    def code_operator_modulus_equal():
        actions.user.vim_insert_mode(" %= ", "a")

    def code_operator_power_equal():
        actions.user.vim_insert_mode(" **= ", "a")

    def code_operator_equal():
        actions.user.vim_insert_mode(" == ", "a")

    def code_operator_not_equal():
        actions.user.vim_insert_mode(" != ", "a")

    def code_operator_great():
        actions.user.vim_insert_mode(" > ", "a")

    def code_operator_less():
        actions.user.vim_insert_mode(" < ", "a")

    def code_operator_great_equal():
        actions.user.vim_insert_mode(" >= ", "a")

    def code_operator_less_equal():
        actions.user.vim_insert_mode(" <= ", "a")

    def code_operator_and():
        actions.user.vim_insert_mode(" && ", "a")

    def code_operator_or():
        actions.user.vim_insert_mode(" || ", "a")

    def code_operator_not():
        actions.user.vim_insert_mode(" !", "a")

    def code_operator_index():
        actions.user.vim_insert_mode("[]", "a")
        actions.insert("h")

    def code_operator_bit_and():
        actions.user.vim_insert_mode(" & ", "a")

    def code_operator_bit_or():
        actions.user.vim_insert_mode(" | ", "a")

    def code_operator_bit_xor():
        actions.user.vim_insert_mode(" ^ ", "a")

    def code_operator_bit_not():
        actions.user.vim_insert_mode(" ~ ", "a")

    def code_operator_bit_left_shift():
        actions.user.vim_insert_mode(" >> ", "a")

    def code_operator_bit_right_shift():
        actions.user.vim_insert_mode(" << ", "a")
