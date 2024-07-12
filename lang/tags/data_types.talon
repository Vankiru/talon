tag: user.code_data_types
-

true:
  user.code_data_type_true()

(false | falls):
  user.code_data_type_false()

(none | nun):
  user.code_data_type_none()

string <user.text>:
  user.code_data_type_string(text)

quote string <user.text>:
  user.code_data_type_quote_string(text)

multi string <user.text>:
  user.code_data_type_multiline_string(text)

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

hash <user.text> to:
  user.code_data_type_hash_pair(text)

hash <user.letter> to:
  user.code_data_type_hash_letter_pair(letter)

hash <user.number> to:
  user.code_data_type_hash_number_pair(number)

(set | said):
  user.code_data_type_set()
