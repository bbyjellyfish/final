# Работа с базой данных

# Задание 1
# Текст задания: "Для этого: выведи список логинов курьеров с количеством их заказов
# в статусе «В доставке» (поле inDelivery = true)."
#Поэтому оставляю в запросе вывод этого поля, ошибку с названием другого поля поправила

SELECT c.login, COUNT(o."inDelivery")
FROM "Couriers" AS c
  JOIN "Orders" AS o ON c.id = o."couriersId"
WHERE o."inDelivery" = True
GROUP BY c.login;

# Задание 2
# Синтаксис поправила, в задании указано: "Для этого: выведи все трекеры заказов и их статусы."
# Поэтому оставляю вывод поля со статусом заказа

SELECT track, finished, cancelled, 'inDelivery'
CASE
WHEN finished = True THEN '2',
WHEN cancelled = True THEN '-1',
WHEN 'inDelivery' = True THEN '1'
ELSE '0'
END
FROM 'Orders';
