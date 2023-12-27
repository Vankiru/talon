title: /vim/
-

talon escape:
  key(escape)
  key(o)
  insert("key(escape)")
  key(escape)

talon (inter | enter):
  key(escape)
  key(o)
  insert("key(enter)")
  key(escape)

talon key <user.letters>:
  key(escape)
  key(o)
  insert("key({letters})")
  key(escape)

talon key <user.word>:
  key(escape)
  key(o)
  insert("key({word})")
  key(escape)

talon key:
  key(escape)
  key(o)
  insert("key()")
  key(left)

talon insert:
  key(escape)
  key(o)
  insert("insert(\"\")")
  key(left)
  key(left)
