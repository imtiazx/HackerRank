SELECT max(salary * months)
    ,count(salary * months)
FROM employee
WHERE salary * months = (
        SELECT max(salary * months)
        FROM employee
        )
