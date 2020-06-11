# 185. Department Top Three Salaries
SELECT tb2.Name AS Department, tb1.Name AS Employee, tb1.Salary
FROM Employee as tb1
INNER JOIN Department as tb2
ON tb1.DepartmentId = tb2.Id
WHERE 3>(SELECT COUNT(DISTINCT tb3.Salary)
          FROM Employee as tb3
          WHERE tb3.Salary > tb1.Salary and tb1.DepartmentId = tb3.DepartmentId
);
