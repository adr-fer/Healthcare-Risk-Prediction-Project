
-- =========================================================
-- KPI 01: High Treatment Cost
-- Business question:
-- Which patient encounters are associated with high costs?
-- Target variable: total_cost_usd
-- =========================================================

-- 1. General target-variable analysis
-- Y variable:
-- total_cost_usd

-- =========================================================
-- 2. DESCRIPTIVE ANALYSIS OF X VARIABLES
-- X variable: 
-- encounter_severity
-- length_of_stay_days
-- adverse_outcome_flag
-- readmitted_30_days_flag
-- polypharmacy_flag
-- opioid_prescribed_flag


-- Total records (the total number of records (rows) in the table)
SELECT COUNT(*) AS total_records
FROM hc_encounters;
             
-- Descriptive statistics for encounter severity
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

-- Descriptive statistics for length_of_stay_days
-- Average, minimum, maximum, and total
SELECT
AVG(length_of_stay_days) AS avg_length_of_stay_days,
MIN(length_of_stay_days) AS min_length_of_stay_days,
MAX(length_of_stay_days) AS max_length_of_stay_days,
SUM(length_of_stay_days) AS total_length_of_stay_days
FROM hc_encounters;

-- Percentage per length_of_stay_days
SELECT
    length_of_stay_days,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hc_encounters) AS percentage
FROM hc_encounters
GROUP BY length_of_stay_days
ORDER BY percentage DESC;

-- -- Total encounters per length_of_stay_days
SELECT
    length_of_stay_days,
    COUNT(*) AS total_encounters
FROM hc_encounters
GROUP BY length_of_stay_days
ORDER BY total_encounters DESC;

-- Standard deviation for length_of_stay_days
SELECT
    STDDEV(length_of_stay_days) AS standard_deviation
FROM hc_encounters;

-- Descriptive statistics for adverse_outcome_flag
-- Average, minimum, maximum, and total
SELECT
AVG(adverse_outcome_flag) AS avg_adverse_outcome_flag,
MIN(adverse_outcome_flag) AS min_adverse_outcome_flag,
MAX(adverse_outcome_flag) AS max_adverse_outcome_flag,
SUM(adverse_outcome_flag) AS total_adverse_outcome_flag
FROM hc_encounters;

-- Rate per length_of_stay_days
SELECT
    AVG(adverse_outcome_flag) * 100 AS readmission_rate
FROM hc_encounters;

-- -- Total encounters per adverse_outcome_flag
SELECT
    adverse_outcome_flag,
    COUNT(*) AS total_adverse_outcome_flag
FROM hc_encounters
GROUP BY adverse_outcome_flag
ORDER BY adverse_outcome_flag DESC;

-- Standard deviation for adverse_outcome_flag
SELECT
    STDDEV(adverse_outcome_flag) AS standard_deviation
FROM hc_encounters;

-- Descriptive statistics for readmitted_30_days_flag
-- Average, minimum, maximum, and total for readmitted_30_days_flag
SELECT
AVG(readmitted_30_days_flag) AS avg_readmitted_30_days_flag,
MIN(readmitted_30_days_flag) AS min_readmitted_30_days_flag,
MAX(readmitted_30_days_flag) AS max_readmitted_30_days_flag,
SUM(readmitted_30_days_flag) AS total_readmitted_30_days_flag
FROM hc_encounters;

-- Rate per readmitted_30_days_flag
SELECT
    AVG(
readmitted_30_days_flag) * 100 AS readmission_rate
FROM hc_encounters;

-- -- Total encounters per readmitted_30_days_flag
SELECT
readmitted_30_days_flag,
COUNT(*) AS total_readmitted_30_days_flag
FROM hc_encounters
GROUP BY readmitted_30_days_flag
ORDER BY readmitted_30_days_flag DESC;

-- Standard deviation for readmitted_30_days_flag
SELECT
    STDDEV(readmitted_30_days_flag) AS standard_deviation
FROM hc_encounters;

-- Descriptive statistics for polypharmacy_flag
-- Average, minimum, maximum, and total for polypharmacy_flag
SELECT
AVG(polypharmacy_flag) AS avg_polypharmacy_flag,
MIN(polypharmacy_flag) AS min_polypharmacy_flag,
MAX(polypharmacy_flag) AS max_polypharmacy_flag,
SUM(polypharmacy_flag) AS total_polypharmacy_flag
FROM hc_encounters;

-- Percentage per polypharmacy_flag
SELECT
    polypharmacy_flag,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hc_encounters) AS percentage
FROM hc_encounters
GROUP BY polypharmacy_flag
ORDER BY percentage DESC;

-- Total encounters per polypharmacy_flag
SELECT
polypharmacy_flag,
COUNT(*) AS total_polypharmacy_flag
FROM hc_encounters
GROUP BY polypharmacy_flag
ORDER BY polypharmacy_flag DESC;

-- Standard deviation for 
SELECT
    STDDEV(polypharmacy_flag) AS standard_deviation
FROM hc_encounters;
-- =========================================================
-- 2. FREQUENCY ANALYSIS OF X VARIABLES
-- encounter_id
-- patient_id
-- facility_id
-- admission_type
-- department
-- primary_diagnosis_group
-- discharge_disposition
