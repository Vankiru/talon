from talon import Context, Module, actions

mod = Module()
mod.list("shell_path", desc="")

ctx = Context()
ctx.matches = "title: /zsh/"

ctx.lists["user.shell_path"] = {
    "home": "",
    "talent": "~/.talon/user",
    "talon": "~/.talon/user",
    "my talon": "~/.talon/user/vankiru",
    "my talent": "~/.talon/user/vankiru",
    "project": "~/projects",
    "projects": "~/projects",
    "gems": "cd ~/projects/gems",
    "talon token": "~/.talon/user/tokeny-talon",
    "token": "~/.vim/plugged/tokeny",
}
