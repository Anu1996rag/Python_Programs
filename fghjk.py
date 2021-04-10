#inputValue =

# class AlphaValidator:
#     def execute():
#         def abc():
#             if "value".isalpha():
#                 return {"result": True, "message": ""}
#             else:
#                 return {"result": False, "message": "Entered value must be a letter."}
#
#         abc()
#
#     #def numberValidate
#
# print(AlphaValidator.execute())
def dict_return(abc):
    ret = {}
    if abc["a"] == 1:
        ret["a"] = abc["a"]
    if abc["b"] == 2:
        ret["b"] = abc["b"]
    else:
        raise AttributeError("Key not found")

    return ret

abc = {
    "a":1,
    "b":2
}

res = dict_return(abc)
a = res["a"]
b = res["b"]

questions = open("questions.txt","r")

question_list = [line.strip() for line in questions]
questions.close()

score = 0
total = len(question_list)
for question in question_list:
    q,a = question.split("=")

    ans = input(f"{q}=")

    if a == ans:
        score +=1


result = open("results.txt","w")
result.write(f"Your final score is {score}/{total}.")
result.close()
