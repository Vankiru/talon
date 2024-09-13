app: iterm2
title: /zsh/
-

slot next:
  key(super-right)

slot last:
  key(super-left)
  
grip clip:
  insert('fgrep -R "')
  edit.paste()
  insert('" ./')
  key(enter)

grip <user.text>:
  insert('fgrep -R "{text}" ')

vim:
  insert("vim")
  key(enter)
