-- Total records (the total number of records (rows) in the table)
SELECT COUNT(*) AS total_records
FROM hc_encounters;

-- Average, minimum, maximum, and total
SELECT
AVG(encounter_severity) AS avg_encounter_severity,
MIN(encounter_severity) AS min_encounter_severity,
MAX(encounter_severity) AS max_encounter_severity,
SUM(encounter_severity) AS total_encounter_severity
FROM hc_encounters;

-- Percentage per encounter_severity
SELECT
    encounter_severity,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hc_encounters) AS percentage
FROM hc_encounters
GROUP BY encounter_severity
ORDER BY percentage DESC;

-- Total encounters per encounters severity level.
SELECT
    encounter_severity,
    COUNT(*) AS total_encounters
FROM hc_encounters
GROUP BY encounter_severity
ORDER BY total_encounters DESC;

-- Standard deviation.
SELECT
    STDDEV(encounter_severity) AS standard_deviation
FROM hc_encounters;
