app: iterm2
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

(catty | katy) home:
  insert("cd")
  key(enter)

(catty | katy) (talent | talon):
  insert("cd ~/.talon/user")
  key(enter)

(catty | katy) my (talent | talon):
  insert("cd ~/.talon/user/vankiru")
  key(enter)

(catty | katy) (project | projects):
  insert("cd ~/projects")
  key(enter)

(catty | katy) gems:
  insert("cd ~/projects/gems")
  key(enter)
