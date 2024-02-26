SELECT i.invoice_id, c.customer_name, i.price, COUNT(co.contact_name) AS contacts_cnt, 
       COALESCE(SUM(CASE WHEN co.contact_email IN (SELECT email FROM customers) THEN 1 ELSE 0 END), 0) AS trusted_contacts_cnt 
FROM invoices AS i 
LEFT JOIN customers AS c ON i.user_id = c.customer_id 
LEFT JOIN contacts AS co ON c.customer_id = co.user_id  
GROUP BY i.invoice_id 
ORDER BY i.invoice_id;
