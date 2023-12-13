# Работа с базой данных

# Задание 1

SELECT c.id, COUNT(."inDelivery")
FROM "Couriers" AS c
JOIN "Orders" AS o ON c.id = o."couriersId"
WHERE o."inDelivery" = True
GROUP BY c.id;

# Задание 2

SELECT track, finished CASE WHEN finished = True THEN '2' ELSE '0'
cancelled CASE WHEN cancelled = True THEN '-1' ELSE '0'
'inDelivery' CASE WHEN 'inDelivery' = True THEN '1' ELSE '0'
FROM 'Orders';
