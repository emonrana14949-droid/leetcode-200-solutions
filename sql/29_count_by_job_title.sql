-- COUNT by Job Title - how many people hold each title.
SELECT job_title, COUNT(*) AS n FROM employees GROUP BY job_title;
