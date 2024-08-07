type = "\%(*\|**\|&\)\="
arg_name = "\<{snake_name}\>"
default = "\s*=\s*{value}"
keyward = ":\s*{value}\=" 
suffix = "\%(,\s*\)\|)\||\)\@="

suffix = "\%(,\s*\|\%()\||\)\@=\)"

arg = "{type}{arg_name}\%({default}\|{keyward}\)\={suffix}"
arg = "\%(*\|**\|&\|\.\.\.\)"

atom_args = "({arg}*)"
atom_barbs = "|{arg}*|"

args = "\%{method_name}\|->\s*\){atom_args}"
barbs = "{\s*{atom_barbs}"


# {name}
# {name} = {value}
# {name}:
# {name}: {value}
# *{name}
# **{name}
# &{name}
# *
# **
# &
# ...

# {arg}, 
# {arg})
# {arg}|

# m(arg, arg)
# m((arg, arg))
# m arg, arg
