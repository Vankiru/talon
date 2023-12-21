app: iterm
-

git undo:
  insert("git undo")
  key(enter)

git discard:
  insert("git discard ")
  edit.paste()
  key(enter)

git (onstage | unstage):
  insert("git unstage")
  key(enter)
