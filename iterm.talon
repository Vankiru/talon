app: iterm2
-

slot next:
  key(super-right)

slot last:
  key(super-left)
  
grip <user.text>:
  insert("fgrep -R \"{text}\" ")
