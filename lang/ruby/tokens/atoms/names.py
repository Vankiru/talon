base_name = "\<\h\w*\>"

variable = base_name
instance_variable = "@{base_name}"
class_variable = "@@{base_name}"
global_variable = "$\%({base_name}\|\d\+\|[!@_\.&~=\/\\*$?]\)"

method = "{base_name}[!?]\="
snake_name = "\(@\|@@\|$\)\=$\%({base_name}\|\d\+\|[!@_\.&~=\/\\*$?]\)[!?]\="

const = "\<\u\(\u\|\d\|_\)*\>"

part_class = "\<\u\w*\>"
class_name = "\%(::\)\={part_class}\%(::{part_class}\)*"
module_name = class_name

name = "\%({snake_name}\|{const_name}\|{class_name}\)"
