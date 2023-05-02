# Practice with function arguments

# Write a super useful function to generate multiplication tables.

# You shoud be able to define the following arguments:

# width (by default 10 -- number of columns)
# height (by default 10 -- number of rows)
# sep_width (by default 3 - width of each column (placeholder for content))
# print_header (by default False - print header "Multiplication Table{width} x {height}" or not)
# NOTE: the dimensions in header should be dynamic (width and height should be substituted with used values)
# print_footer (by default True - print footer in form of line of 30 "-" characters)
# NOTE:

# sep_width = 3 means that we have the following columns (with . as space):

# ..1..2..3.10.12.13

# sep_width = 4 means that we have the following columns (with . as space):

# ...1...2...3..10..11..12

# Additionally:

# sep_width, print_header and print_footer should be keyword-only arguments.
# Note that the function gen_mul_table should return a multi-line string with the table. Also please note that it should not end with "\n".