import numpy as np


def calculate_sum_all_products_in_order(list_of_objects):
    total_price_overall = 0
    for ordered_product in list_of_objects:
        price = ordered_product.price
        amount = ordered_product.amount
        print('price ', price, ' i amount ', amount)
        total_price_overall += price * amount
    return total_price_overall


# def calculate_total_amount_products_order(object):
#     for ordered_product in object:
#         product_price_list.append(ordered_product.price)
#         product_list_amount.append(ordered_product.amount)
#     total_price = None
#     print(' to type', type(product_list_amount), ' i typ 1 recordu', type(product_list_amount[0]))
#     print(' to type', type(product_price_list), ' i typ 1 recordu', type(product_price_list[0]))
#     # product_calculated_list = product_list_amount * product_price_list
#     return product_calculated_list


# a = np.array([1,2,3,4])
# b = np.array([2,3,4,5])
# a * b
# array([ 2,  6, 12, 20])

#  lub
# [a*b for a,b in zip(lista,listb)]