tag: user.code_data_types
-

true:
  user.code_data_type_true()

(false | falls):
  user.code_data_type_false()

(none | nun):
  user.code_data_type_none()

number <user.number_string>:
  user.vim_insert_mode(number_string, "a")

number <user.number_string> point <user.number_string>:
  user.vim_insert_mode("{number_string_1}.{number_string_2}", "a")

string <user.text>:
  user.code_data_type_string(text)

string:
  user.code_data_type_empty_string()

quote string <user.text>:
  user.code_data_type_quote_string(text)

quote string:
  user.code_data_type_empty_quote_string()

multi string <user.text>:
  user.code_data_type_multiline_string(text)

multi string:
  user.code_data_type_empty_multiline_string()

interpol <user.variable_name>:
  user.code_data_types_string_interpolation(variable_name)

interpol:
  user.code_data_types_empty_string_interpolation()

list:
  user.code_data_type_list()

multi list:
  user.code_data_type_multiline_list()

object list:
  user.code_data_type_object_list()

hash:
  user.code_data_type_hash()

multi hash:
  user.code_data_type_multiline_hash()

object hash:
  user.code_data_type_object_hash()

key <user.key_name> [to]:
  user.code_data_type_key_value(key_name)

(set | said):
  user.code_data_type_set()
