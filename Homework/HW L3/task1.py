from string import Template

name = "Vitalii"
day = "26 June"

# % Operator
print("Good day %s! %s is a perfect day to learn some python." % (name, day))

# str.format
print("Good day {}! {} is a perfect day to learn some python.".format(name, day))

# f-Strings
print(f"Good day {name}! {day} is a perfect day to learn some python.")

# Template Strings
t = "Good day $name! $day is a perfect day to learn some python."
print(Template(t).substitute(name=name, day=day))