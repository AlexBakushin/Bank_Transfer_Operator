from funcions import Operations, opener_zip, is_executed

#Создание отсортированного массива из архива
operations_list_list = opener_zip()
#Фильтрация массива
executed_list = is_executed()
#Итерация массива на отдельные операции
for one_division in executed_list:
    #Деление информации об операции на составляющие
    id_, state, data, operation_amount, description, from_, to = one_division
    #Перенос составляющих в класс
    operation_1 = Operations(id_, state, data, operation_amount, description, from_, to)
    #Печать результата
    operation_1.print()
