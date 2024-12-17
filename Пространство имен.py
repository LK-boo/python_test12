def test_function():
    def inner_function():
        call = "Я в области видимости функции test_function"
        print(call)
    inner_function()
test_function()
#inner_function()