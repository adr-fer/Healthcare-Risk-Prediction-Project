
-- =========================================================
-- KPI 01: High Treatment Cost
-- Business question:
-- Which patient encounters are associated with high costs?
-- Target variable: total_cost_usd
-- =========================================================

-- 1. General target-variable analysis
-- Y variable:
-- total_cost_usd

-- Total number of unique treatment-cost values
SELECT COUNT(DISTINCT total_cost_usd) AS unique_cost_values
FROM hc_encounters;

-- Avg, Max, Min of treatment cost
SELECT
AVG(total_cost_usd) AS avg_total_cost_usd,
MIN(total_cost_usd) AS min_total_cost_usd,
MAX(total_cost_usd) AS max_total_cost_usd,
FROM hc_encounters;

-- Sum of treatment cost
SELECT
    CAST(ROUND(SUM(total_cost_usd), 2) AS DECIMAL(18,2))
        AS total_treatment_cost
FROM hc_encounters;

-- Standard deviation for treatment cost 
SELECT
    STDDEV(total_cost_usd) AS standard_deviation
FROM hc_encounters;

-- Distribution for treatment cost
SELECT
    CASE
WHEN total_cost_usd < 5261.73 THEN '$2,227.00–$5,261.72'
WHEN total_cost_usd < 8296.45 THEN '$5,261.73–$8,296.44'
WHEN total_cost_usd < 11331.18 THEN '$8,296.45–$11,331.17'
ELSE '$11,331.18–$14,365.90'
        
    END AS value_range,

    COUNT(*) AS frequency,

    COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER () AS percentage

FROM hc_encounters
WHERE total_cost_usd IS NOT NULL

GROUP BY 1
ORDER BY 1;

-- Percentiles/quartiles for treatment cost
SELECT
    approx_percentile(total_cost_usd, 0.25) AS q1_25th_percentile,
    approx_percentile(total_cost_usd, 0.50) AS q2_median,
    approx_percentile(total_cost_usd, 0.75) AS q3_75th_percentile
FROM hc_encounters
WHERE total_cost_usd IS NOT NULL;
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

-- Total encounters per length_of_stay_days
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

-- Rate per adverse_outcome_flag
SELECT
    AVG(adverse_outcome_flag) * 100 AS adverse_outcome_rate
FROM hc_encounters;

-- Total encounters per adverse_outcome_flag
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

-- Total encounters per readmitted_30_days_flag
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

-- Rate per polypharmacy_flag
SELECT
    AVG(polypharmacy_flag) * 100 AS polypharmacy_rate
FROM hc_encounters;

-- Total encounters per polypharmacy_flag
SELECT
polypharmacy_flag,
COUNT(*) AS total_polypharmacy_flag
FROM hc_encounters
GROUP BY polypharmacy_flag
ORDER BY polypharmacy_flag DESC;

-- Standard deviation for polypharmacy_flag
SELECT
    STDDEV(polypharmacy_flag) AS standard_deviation
FROM hc_encounters;

-- Descriptive statistics for opioid_prescribed_flag
-- Average, minimum, maximum, and total for opioid_prescribed_flag   
SELECT
AVG(opioid_prescribed_flag) AS avg_opioid_prescribed_flag,
MIN(opioid_prescribed_flag) AS min_opioid_prescribed_flag,
MAX(opioid_prescribed_flag) AS max_opioid_prescribed_flag,
SUM(opioid_prescribed_flag) AS total_opioid_prescribed_flag
FROM hc_encounters;

-- Rate per opioid_prescribed_flag
SELECT
    AVG(opioid_prescribed_flag) * 100 AS opioid_prescription_rate
FROM hc_encounters;

-- Total encounters per opioid_prescribed_flag
SELECT
opioid_prescribed_flag,
COUNT(*) AS total_opioid_prescribed_flag
FROM hc_encounters
GROUP BY opioid_prescribed_flag
ORDER BY opioid_prescribed_flag DESC;

-- Standard deviation for opioid_prescribed_flag
SELECT
    STDDEV(opioid_prescribed_flag) AS standard_deviation
FROM hc_encounters;
-- =========================================================
-- 2. FREQUENCY ANALYSIS OF X VARIABLES
-- admission_type
-- Unique value count by admission_type

SELECT
    COUNT(admission_type) AS total_admission_type_observations,
    COUNT(DISTINCT admission_type ) AS unique_admission_type_values
FROM hc_encounters;

-- Total count by admission_type 

SELECT
    admission_type,
    COUNT(*) AS total_admission_type
FROM hc_encounters
GROUP BY admission_type
ORDER BY total_admission_type DESC

-- Percentage per value by admission_type
SELECT
    admission_type,
    COUNT(*) AS total_admission_type
FROM hc_encounters
GROUP BY admission_type
ORDER BY total_admission_type DESC;

-- department
-- Unique value count by department
SELECT
    COUNT(department) AS total_department_observations,
    COUNT(DISTINCT department ) AS unique_department_values
FROM hc_encounters;

-- Total count by department
SELECT
    department,
    COUNT(*) AS total_department
FROM hc_encounters
GROUP BY department
ORDER BY total_department DESC;

-- Percentage per value by department 
SELECT
    department,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hc_encounters) AS percentage
FROM hc_encounters
GROUP BY department
ORDER BY percentage DESC;

-- primary_diagnosis_group
-- Unique value count by primary_diagnosis_group
SELECT
    COUNT(primary_diagnosis_group) AS total_primary_diagnosis_group_observations,
    COUNT(DISTINCT department ) AS unique_primary_diagnosis_groupt_values
FROM hc_encounters;

-- Total count by primary_diagnosis_group

SELECT
    primary_diagnosis_group,
    COUNT(*) AS total_department
FROM hc_encounters
GROUP BY primary_diagnosis_group
ORDER BY primary_diagnosis_group DESC;

-- Percentage per value by primary_diagnosis_group
SELECT
    primary_diagnosis_group,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM hc_encounters) AS percentage
FROM hc_encounters
GROUP BY primary_diagnosis_group
ORDER BY percentage DESC;


-- discharge_disposition



