"help('keyword')"
import keyword
print(keyword.iskeyword("True"))
print(keyword.iskeyword("Import"))
print(keyword.iskeyword("ELSE"))
print(keyword.iskeyword("if"))
print(keyword.iskeyword("int")) 


print('num1'.isidentifier())
print('9a'.isidentifier())
print('a_1'.isidentifier())
print('_1a'.isidentifier())
print('a+'.isidentifier())
