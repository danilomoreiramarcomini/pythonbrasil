# https://wiki.python.org.br/EstruturaDeDecisao

value_of_the_first_product = float(input("First product: "))
value_of_the_second_product = float(input("Second product: "))
third_of_the_first_product = float(input("Third product: "))

if value_of_the_first_product < value_of_the_second_product and value_of_the_first_product < third_of_the_first_product:
    print(f"Buy the product with value of $:\033[34m{value_of_the_first_product}\033[38m")
elif value_of_the_second_product < value_of_the_first_product and value_of_the_second_product < \
        third_of_the_first_product:
    print(f"Buy the product with value of $:\033[34m{value_of_the_second_product}\033[38m")
elif third_of_the_first_product < value_of_the_first_product and third_of_the_first_product < \
        value_of_the_second_product:
    print(f"Buy the product with value of$:\033[34m{third_of_the_first_product}\033[38m")
