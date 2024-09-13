app: iterm2
title: /zsh/
-

slot next:
  key(super-right)

slot last:
  key(super-left)
  
grip <user.text>:
  insert("fgrep -R \"{text}\" ")

vim:
  insert("vim")
  key(enter)
