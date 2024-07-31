# Ruby

- [Arguments](#arguments)
- [Blocks](#blocks)
- [Classes](#classes)
- [Comments](#comments)
- [Controls](#controls)
- [Data Types](#data-types)
- [Exceptions](#exceptions)
- [Library](#library)
- [Methods](#methods)
- [Modules](#modules)
- [Names](#names)
- [Operators](#operators)
- [Statements](#statements)

## Arguments

```ruby
# arts
()
# barbs
 ||
# left art
(
# right art
)
# comma
, 
# line comma
,\n
# default <variable_name> [to]
variable_name: 
# list art <variable_name>
*variable_name
# hash art <variable_name>
**variable_name
# key art <variable_name>
variable_name:
# block art <variable_name>
&variable_name
# forward art
...
```

## Blocks
```ruby
# block
 do
end

# line block
 {  }
```

## Classes

```ruby
# class <class_name>
class ClassName
end

# self class
class << self
end

# superclass <class_name>
 < ClassName

# class init
def initialize
end

# private
private
# protected
protected
# public
public

# new <class_name>
ClassName.new
```

## Comments

```ruby
# remark <text>
# text

# line remark <text>
<code> # text

# multi remark <text>
=begin
text
=end

# frozen string
# frozen_string_literal: true

# magic encode
# encoding: 

# magic warn
# warn_indent: true

# magic share none
# shareable_constant_value: none

# magic share lit
# shareable_constant_value: literal

# magic share every
# shareable_constant_value: experimental_everything

# magic share copy
# shareable_constant_value: experimental_copy
```

## Controls

```ruby
# if
if 
end

# else
else

# else if
elsif 

# unless
unless 
end

# leaf
 if 

# unleaf
 unless

# triplet
 ?  : 

# case
case 
end

# when
when 

# then
 then

# while
while  do
end

# until
until  do
end

# end while
begin
end while

# line while
 while

# line until
 until

# for <item> in <list>
for item in list do
end

# break
break
# break if
break if 
# next
next
# next if
next if 
```

## Data Types

```ruby
# true
true
# false
false
# none | nun
nil

# number <number> 
12
# number <number> point <number>
12.34

# string <text>
"text"
# quote string <text>
'text'
# multi string <text>
"
text
"
# interpol <variable_name>
#{variable_name}
# interpol
#{}
# doc string <text>
<<~DOC
text
DOC

# sim <variable_name>
:variable_name

# list
[]
# multi list
[
]
# object list
Array.new()
# string list
%w[]
# sim list
%i[]

# hash
{}
# multi hash
{
}
# object hash
Hash.new()
# key <key> to
key: 
# string key <key> to
"key": 
# object key <key> to
key => 

# set
Set.new()

# range <from> to <to>
(from..to)
# range <from> until <to>
(from...to)
# range <from>
(from..)
# range to <to>
(..to)
# range until <to>
(...until)
# object range <from> to <to>
Range.new(from, to)
# object range <from> until <to>
Range.new(from, to, true)

# rig <text>
/text/

# lambda
-> {  }
```

# Exceptions

```ruby
# raise <class_name>
raise ClassName

# error <class_name>
ClassNameError

# begin
begin
end

# rescue
rescue
# rescue <class_name>
rescue ClassName
# rescue as <variable_name>
rescue => variable_name
# rescue <class_name> as <variable_name>
rescue ClassName => variable_name

# ensure
ensure
# retry
retry
```

## Library

```ruby
# print <text>
puts "text"
```

## Methods

```ruby
# met <method_name>
def method_name
end

# short met <method_name>
def <method_name> = 

# met bank | mukbang <method_name>
def method_name!
end

# met plight <method_name>
def method_name?
end

# return
return
# parent
super
# yeild
yield
# yeild self
yeild self

# call <method_name>
.method_name
# call bang <method_name>
.method_name!
# call plight <method_name>
.method_name?
# safe call <method_name>
&.method_name
```

## Modules

```ruby
# module <module_name>
module ModuleName
end

# refine <class_name>
refine ClassName
end

# include <module_name>
include ModuleName
# extend <module_name>
extend ModuleName
# using <module_name>
using ModuleName
```

## Names

```ruby
# name <variable_name>
variable_name
# bang <method_name>
method_name!
# plight <method_name>
method_name?

# instance <variable_name>
@variable_name
# type instance <variable_name>
@@variable_name

# self <variable_name>
self.variable_name

# const <const_name>
CONST_NAME

# type <class_name>
ClassName
# pack <class_name>
::ClassName

# global <variable_name>
$variable_name
```

## Operators

```ruby
# set to
 = 
# set <variable_name> to
variable_name = 

# plus
 + 
# minus
 - 
# multi
 * 
# divide
 / 
# modulus
 % 
# power
**

# plus equal
 += 
# minus equal
 -= 
# multi equal
 -= 
# divide equal
 /= 
# mod equal
 %= 
# power equal
 **= 

# equal
 == 
# not equal
 != 
# great
 > 
# lest
 < 
# great equal
 >= 
# lest equal
 <= 
# compare
 <=>
# test equal
 === 

# add | also
 && 
# or | either
 || 
# not
 !
# text add | also
 and 
# text or | either
 or 
# text not
 not

# index
[]
# inside
 in 
# match
 => 

# bit and
 & 
# bit or
 | 
# bit ex
 ^ 
# bit not
 ~ 
# bit left
 << 
# bit right
 >> 
```

## Statements

```ruby
# require <path>
require "path"

# alias <method_name> to <method_name>
alias method_name method_name

# unbind <method_name>
undef method_name

# defined <method_name>
defined?(method_name)

# art read
attr_reader 
# art write
attr_writter 
# art access
attr_accessor 
```
