from funcions import Operations, opener_zip, is_executed

operations_list_list = opener_zip()
executed_list = is_executed()
for one_division in executed_list:
    id_, state, data, operation_amount, description, from_, to = one_division
    operation_1 = Operations(id_, state, data, operation_amount, description, from_, to)
    operation_1.print()
