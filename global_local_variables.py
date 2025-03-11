global_variable=10
def variable1(global_variable):
    print("global variable inside function:",global_variable)
var1=variable1(global_variable)
print("global variable outside the function:",global_variable)
"""def variable2():
    local_variable=5
    print("local variable inside the function:",local_variable)
var2=variable2()
print("local variable outside of function :",local_variable)"""#shows error because local variable available inside the function
