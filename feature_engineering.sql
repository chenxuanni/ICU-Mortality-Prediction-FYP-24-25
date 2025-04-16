ALTER TABLE icu_vital_diagnoses
ADD COLUMN icu_unit_micu INT,
ADD COLUMN icu_unit_sicu INT,
ADD COLUMN icu_unit_ccu INT;

UPDATE icu_vital_diagnoses
SET 
    icu_unit_micu = CASE WHEN icu_unit = 'MICU' THEN 1 ELSE 0 END,
    icu_unit_sicu = CASE WHEN icu_unit = 'SICU' THEN 1 ELSE 0 END,
    icu_unit_ccu = CASE WHEN icu_unit = 'CCU' THEN 1 ELSE 0 END;
ALTER TABLE icu_vital_diagnoses
ADD COLUMN heart_rate_scaled FLOAT,
ADD COLUMN blood_pressure_scaled FLOAT,
ADD COLUMN oxygen_saturation_scaled FLOAT;

UPDATE icu_vital_diagnoses
SET 
    heart_rate_scaled = (heart_rate - (SELECT MIN(heart_rate) FROM icu_vital_diagnoses)) /
                        ((SELECT MAX(heart_rate) FROM icu_vital_diagnoses) - (SELECT MIN(heart_rate) FROM icu_vital_diagnoses)),

    blood_pressure_scaled = (blood_pressure - (SELECT MIN(blood_pressure) FROM icu_vital_diagnoses)) /
                            ((SELECT MAX(blood_pressure) FROM icu_vital_diagnoses) - (SELECT MIN(blood_pressure) FROM icu_vital_diagnoses)),

    oxygen_saturation_scaled = (oxygen_saturation - (SELECT MIN(oxygen_saturation) FROM icu_vital_diagnoses)) /
                                ((SELECT MAX(oxygen_saturation) FROM icu_vital_diagnoses) - (SELECT MIN(oxygen_saturation) FROM icu_vital_diagnoses));
