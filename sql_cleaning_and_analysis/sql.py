--create and import table from excel sheet

CREATE TABLE Bolivia (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);

CREATE TABLE Costa_Rica (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);


CREATE TABLE Mexico (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);

CREATE TABLE Guatemala (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);

CREATE TABLE Ecuador (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);


CREATE TABLE El Salvador (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);


CREATE TABLE Nicaragua (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);



CREATE TABLE India (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);


CREATE TABLE Panama (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);


CREATE TABLE Peru (
    id serial PRIMARY KEY,
    Destination TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Category TEXT,
    Quantity NUMERIC,
	Unit_Cost NUMERIC,
	Local_Currency NUMERIC,
	Pound_Sterling NUMERIC,
	Total_Spending NUMERIC
);

-- clean data for ecuador
UPDATE ecuador
SET
    quantity = '1',
    unit_cost = '0',
    local_currency = '0'
WHERE
    quantity IS NULL
    OR unit_cost IS NULL
    OR local_currency IS NULL;

-- update table el_salvador
ALTER TABLE el_salvador
ALTER COLUMN quantity TYPE INTEGER;

-- update table bolivia
ALTER TABLE bolivia
ALTER COLUMN quantity TYPE INTEGER;

UPDATE bolivia
SET date = '2023-10-17'
WHERE date = '2024-10-17';

UPDATE bolivia
SET date = '2023-10-18'
WHERE date = '2024-10-18';

UPDATE bolivia
SET date = '2023-10-19'
WHERE date = '2024-10-19';

UPDATE bolivia
SET date = '2023-10-20'
WHERE date = '2024-10-20';

UPDATE bolivia
SET category = 'Grocery'
WHERE category = 'Grocerries';

UPDATE bolivia
SET category = 'Activities'
WHERE category = 'Dating';

-- amend incorrect data input for guatemala
UPDATE guatemala
SET date = '2024-03-25'
WHERE date = '2023-03-25';

UPDATE guatemala
SET date = '2024-03-26'
WHERE date = '2023-03-26';

-- incorrect update for india
ALTER TABLE india
ALTER COLUMN quantity TYPE INTEGER;

UPDATE india
SET quantity = '0'
WHERE quantity IS NULL;

BEGIN;

-- update statement
UPDATE india
SET quantity = '0'
WHERE quantity IS NULL;

-- undo the update
ROLLBACK;

-- correct version
SELECT *
FROM india
WHERE category = 'Null'; -- cannot use IS NULL function here because Null is a string

UPDATE india
SET quantity = 0
WHERE category = 'Null';

UPDATE india
SET category = 'Activities'
WHERE category = 'Null';

-- update mexico
UPDATE mexico
SET category = 'Grocery'
WHERE category = 'Grocerries'

-- update nicaragua
ALTER TABLE nicaragua
ALTER COLUMN quantity TYPE INTEGER;

-- amend incorrect data input for nicaragua
UPDATE nicaragua
SET date = '2024-02-20'
WHERE date = '2021-02-20';

-- update panama
UPDATE panama
SET category = 'Activities'
WHERE category = 'Null';

-- update peru
ALTER TABLE peru
ALTER COLUMN quantity TYPE INTEGER;

-- union all 10 tables
WITH new_table AS (
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM bolivia
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM costa_rica
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM ecuador
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM el_salvador
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM guatemala
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM india
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM mexico
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM nicaragua
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM panama
	UNION ALL
	SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending FROM peru
	)

-- to calculate the total spending and daily average
SELECT
    ((DATE '2024-08-01' - DATE '2024-07-09') + (DATE '2024-04-15' - DATE '2023-10-13')) AS total_days,
    SUM(pound_sterling) AS total_spending,
    ROUND(SUM(pound_sterling) / (
    ((DATE '2024-08-01' - DATE '2024-07-09') + (DATE '2024-04-15' - DATE '2023-10-13'))
), 2) AS daily_average
FROM new_table;

-- combine all data together to achieve readability
WITH combined_data AS (
    SELECT 'Bolivia' AS country, category, SUM(pound_sterling) AS total_per_category, DATE '2023-11-09' - DATE '2023-10-12' AS days
    FROM bolivia
    GROUP BY category

    UNION ALL

    SELECT 'Costa Rica', category, SUM(pound_sterling), DATE '2024-02-16' - DATE '2024-02-13'
    FROM costa_rica
    GROUP BY category

    UNION ALL

    SELECT 'Ecuador', category, SUM(pound_sterling), DATE '2024-02-02' - DATE '2023-12-20'
    FROM ecuador
    GROUP BY category

    UNION ALL

    SELECT 'El Salvador', category, SUM(pound_sterling), DATE '2024-03-04' - DATE '2024-02-27'
    FROM el_salvador
    GROUP BY category

    UNION ALL

    SELECT 'Guatemala', category, SUM(pound_sterling), DATE '2024-03-26' - DATE '2024-03-05'
    FROM guatemala
    GROUP BY category

    UNION ALL

    SELECT 'India', category, SUM(pound_sterling), DATE '2024-08-01' - DATE '2024-07-09'
    FROM india
    GROUP BY category

    UNION ALL

    SELECT 'Mexico', category, SUM(pound_sterling), DATE '2024-04-15' - DATE '2024-03-27'
    FROM mexico
    GROUP BY category

    UNION ALL

    SELECT 'Nicaragua', category, SUM(pound_sterling), DATE '2024-02-26' - DATE '2024-02-17'
    FROM nicaragua
    GROUP BY category

    UNION ALL

    SELECT 'Panama', category, SUM(pound_sterling), DATE '2024-02-12' - DATE '2024-02-03'
    FROM panama
    GROUP BY category

    UNION ALL

    SELECT 'Peru', category, SUM(pound_sterling), DATE '2023-12-19' - DATE '2023-11-10'
    FROM peru
    GROUP BY category
)

-- to work out the total spending per country
SELECT country,
       SUM(total_per_category) AS total_per_country,
       ROUND(MAX(days)) AS days,
	   ROUND(SUM(total_per_category)/(MAX(days)), 2) AS average_per_day
FROM combined_data
GROUP BY country
ORDER BY average_per_day DESC;

-- to work out total spending per category
SELECT category, SUM(total_per_category) AS total_spending
FROM combined_data
GROUP BY category
ORDER BY total_spending DESC;

-- to work out total spending per category for each country (comparison of countries)
SELECT country, category, SUM(total_per_category) AS total_per_category
FROM combined_data
GROUP BY country, category
ORDER BY country, total_per_category DESC;

-- to work out the total spending per country
SELECT country, SUM(total_per_category) AS total_per_country
FROM combined_data
GROUP BY country
ORDER BY country, total_per_country DESC;

COPY (
    WITH new_table AS (
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM bolivia
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM costa_rica
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM ecuador
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM el_salvador
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM guatemala
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM india
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM mexico
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM nicaragua
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM panama
        UNION ALL
        SELECT destination, date, description, category, quantity, unit_cost, local_currency, pound_sterling, total_spending
        FROM peru
    )
    SELECT * FROM new_table
) TO '/Users/samsamchua/Desktop/Personal Project/Postgres_SQL_query.csv'
WITH CSV HEADER;

