inputValue = "@"

class AlphaValidator:
    def execute(value):
        inputValue = value
        if inputValue.isalpha():
            return {"result": True, "message": ""}
        else:
            return {"result": False, "message": "Entered value must be a letter."}

class NumberValidator:
    def execute(value):
        inputValue = value
        if inputValue.isnumeric():
            return {"result": True, "message": ""}
        else:
            return {"result": False, "message": "Entered value must be a number."}

class AlphaNumericValidator:
    def execute(value):
        inputValue = value
        if inputValue.isalnum():
            return {"result": True, "message": ""}
        else:
            return {"result": False, "message": "Entered value must be a alphanumeric."}

    #def numberValidate

print(AlphaValidator.execute(inputValue))
print(NumberValidator.execute(inputValue))
print(AlphaNumericValidator.execute(inputValue))
