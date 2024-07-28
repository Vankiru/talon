tag: user.code_operators
-

plus:
  user.code_operator_plus()

minus:
  user.code_operator_minus()

multi:
  user.code_operator_multiplication()

divide:
  user.code_operator_division()

(mode | modulus):
  user.code_operator_modulus()

power:
  user.code_operator_exponent()

(set | said) (to | two):
  user.code_operator_set_to()

set <user.variable_name> [to]:
  user.code_operator_set_variable_to(variable_name)

plus equal:
  user.code_operator_plus_equal()

minus equal:
  user.code_operator_minus_equal()

multi equal:
  user.code_operator_multi_equal()

divide equal:
  user.code_operator_divide_equal()

(mode | modulus) equal:
  user.code_operator_modulus_equal()

power equal:
  user.code_operator_power_equal()

equal:
  user.code_operator_equal()

not equal:
  user.code_operator_not_equal()

great:
  user.code_operator_great()

less:
  user.code_operator_less()

great equal:
  user.code_operator_great_equal()

less equal:
  user.code_operator_less_equal()

(add | also):
  user.code_operator_and()

(or | either):
  user.code_operator_or()

not:
  user.code_operator_not()

index:
  user.code_operator_index()

bit (and | add | also):
  user.code_operator_bit_and()

bit (or | either):
  user.code_operator_bit_or()

bit ex:
  user.code_operator_bit_xor()

bit not:
  user.code_operator_bit_not()

bit left:
  user.code_operator_bit_left_shift()

bit right:
  user.code_operator_bit_right_shift()
