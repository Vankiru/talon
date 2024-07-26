title: /\w*\.rb (.*) - VIM/
-

tag(): user.code_classes

class <user.text>:
  user.code_class_with_name(text)

superclass <user.text>:
  user.code_superclass_with_name(text)

new <user.text>:
  user.code_class_new(text)
