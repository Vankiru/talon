app: iterm2
-

slot next:
  key(super-right)

slot last:
  key(super-left)
  
grip <user.text>:
  insert("fgrep -R \"{text}\" ")

(catty | katy) home:
  insert("cd")
  key(enter)

(catty | katy) (talent | talon):
  insert("cd /Users/vankiru/.talon/user")
  key(enter)

(catty | katy) my (talent | talon):
  insert("cd /Users/vankiru/.talon/user/vankiru")
  key(enter)

(catty | katy) one:
  insert("cd /Users/vankiru/projects/crestar/lendingone")
  key(enter)
