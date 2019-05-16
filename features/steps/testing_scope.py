from behave import *


@given('preset "{val}"')
def set_var(context, val=0):
    context.var = int(val)


@when('set "{val}"')
def set_var(context, val=-1):
    write_to_file("\nvar = " + str(context.var) + " + " + str(val) + " = ")
    context.var = int(context.var) + int(val)
    write_to_file(str(context.var))


@then('eq "{val}"')
def assert_val(context, val=-1):
    write_to_file("\nassert: " + str(context.var) + " = " + str(val))
    assert int(context.var) == int(val)


def write_to_file(string_to_write):
    f = open("log.txt", 'a')
    f.write(string_to_write)
    f.close()
