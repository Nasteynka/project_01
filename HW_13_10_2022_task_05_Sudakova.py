# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000
i=0
k = 0
while i <12:
    k = k + (expenses*(1.03**i))
    #k = k + (expenses*(1.03**i)-salary)
    i +=1
all_salary = salary*(i)
live = abs(all_salary - k)
print("Необходимо занять ", round(live,2),'рублей')
    



   
