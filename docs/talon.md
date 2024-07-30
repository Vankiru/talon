# Talon

## .talon

### Context

```python
# code talon
title: /\w*\.talon (.*) - VIM/

# code python
title: /\w*\.py (.*) - VIM

# code ruby
title: /\w*\.rb (.*) - VIM

# context tag <tag_name>
tag: user.<tag_name>

# header | body
-

```

### Body

```python
# body tag <tag_name>
tag(): user.<tag_name>

# rule <rule_name>
<rule_name>:
```

### Keys

```python
# talon escape
key(escape)

# talon (inter | enter)
key(enter)

# talon key <letters>
key(<letters>)

# talon key <word>
key(<word>)

# talon key
key()

# talon insert
insert("")
```

### Captures

```python
# capture letter
 <user.letter>

# capture letters
 <user.letters>

# capture word
 <user.word>

# capture text
 <user.text>

# capture number
 <user.number_string>

# capture anna
 <user.code_annotation_type>

# capture ruby class
 <user.code_ruby_class_name>
```

### Actions

```python
# user action <action_name>
user.<action_name>()

# format snake <variable_name>
<variable_name> = user.code_snake_case(text)

# format scream <variable_name>
<variable_name> = user.code_screaming_case(text)

# format camel <variable_name>
<variable_name> = user.code_camel_case(text)
```

### Vim Actions

```python
# vim normal <letters>
user.vim_normal_mode("<letters>")

# vim normal
user.vim_normal_mode("")

# vim key <letters>
user.vim_normal_mode_key("<letters>")

# vim key
user.vim_normal_mode_key("")

# vim insert
user.vim_insert_mode("", "i")

# vim insert after
user.vim_insert_mode("", "a")

# vim insert below
user.vim_insert_mode("", "o")

# vim insert above
user.vim_insert_mode("", "O")

# vim visual <letters>
user.vim_visual_mode("<letters>")

# vim visual
user.vim_visual_mode("")

# vim vertical <letters>
user.vim_vertical_visual_mode("<letters>")

# vim vertical
user.vim_vertical_visual_mode("")

# vim (comment | command) <letters>
user.vim_command_mode("<letters>")

# vim (comment | command)
user.vim_command_mode("")
```

## .py

### Structure

```python
# talon import
from talon import Context, Module, actions

# talon import (module | model)
from talon import Module

# talon import context
  from talon import Context, actions

# talon new (module | model)
mod = Module()

# talon new context
ctx = Context()

# talon context match
ctx.matches = ""

# talon context vim
ctx.matches = "title: /VIM/"

# talon context ruby
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

# talon context python
ctx.matches = "title: /\w*\.py (.*) - VIM/"

# talon (module | model) actions
@mod.action_class
class Actions:
  pass

# talon <name> actions
@ctx.action_class("user")
class <Name>Actions:
  pass
```

### Templates

```python
# talon vim file
from talon import Context, Module, actions

mod = Module()
ctx = Context()
ctx.matches = "title: /VIM/"

@mod.action_class
class Actions:
  pass

@ctx.action_class("user")
class VimActions:
  pass

# talon ruby file
from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.rb (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
  pass

# talon python file
from talon import Context, actions

ctx = Context()
ctx.matches = "title: /\w*\.py (.*) - VIM/"

@ctx.action_class("user")
class CodeActions:
  pass

# talong tag file
from talon import Module

mod = Module()
mod.tag("", desc="")

@mod.action_class
class Actions:
  pass
```

### Actions

```python
# user action <action_name>
actions.user.<action_name>()

# format snake <variable_name>
<variable_name> = actions.user.code_snake_case(text)

# format scream <variable_name>
<variable_name> = actions.user.code_screaming_case(text)

# format camel <variable_name>
<variable_name> = actions.user.code_camel_case(text)
```

### Keys

```python
# talon escape
actions.key(escape)

# talon (inter | enter)
actions.key(enter)

# talon key <letters>
actions.key(<letters>)

# talon key <word>
actions.key(<word>)

# talon key
actions.key()

talon insert
actions.insert("")
```

### Vim Actions

```python
# vim normal <letters>
actions.user.vim_normal_mode("<letters>")

# vim normal
actions.user.vim_normal_mode("")

# vim key <letters>
actions.user.vim_normal_mode_key("<letters>")

# vim key
actions.user.vim_normal_mode_key("")

# vim insert
actions.user.vim_insert_mode("", "i")

# vim insert after
actions.user.vim_insert_mode("", "a")

# vim insert below
actions.user.vim_insert_mode("", "o")

# vim insert above
actions.user.vim_insert_mode("", "O")

# vim visual <letters>
actions.user.vim_visual_mode("<letters>")

# vim visual
actions.user.vim_visual_mode("")

# vim vertical <letters>
actions.user.vim_vertical_visual_mode("<letters>")

# vim vertical
actions.user.vim_vertical_visual_mode("")

# vim (comment | command) <letters>
actions.user.vim_command_mode("<letters>")

# vim (comment | command)
actions.user.vim_command_mode("")
```

