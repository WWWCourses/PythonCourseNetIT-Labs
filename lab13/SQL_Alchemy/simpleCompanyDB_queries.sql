SELECT	employee_name,company_name
FROM employee
JOIN company_employee
	ON (company_employee.employee_id=employee.employee_id)
JOIN company
	ON (company_employee.company_id=company.company_id);
