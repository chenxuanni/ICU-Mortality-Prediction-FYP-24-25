-- extract_vitals.sql
SELECT subject_id, hadm_id, charttime, value
FROM chartevents
WHERE itemid IN (220045, 220179, 220210);

-- merge_icu_stays.sql
SELECT icu.subject_id, icu.hadm_id, icu.stay_id, adm.hospital_expire_flag
FROM icustays icu
LEFT JOIN admissions adm ON icu.hadm_id = adm.hadm_id;
