# this program checks for the input type

class InputTypeValidator:
    def execute(value):
        inputValue = value
        if type(inputValue) == int:
            return {"result": True, "message": ""}
        else:
            return {"result": False, "message": "Entered value must be a number."}

print(InputTypeValidator.execute("10"))