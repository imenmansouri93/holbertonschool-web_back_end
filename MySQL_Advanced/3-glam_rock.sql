-- best band_name
SELECT band_name, 
       CASE 
          WHEN formed IS NOT NULL AND split IS NOT NULL THEN split - formed
          WHEN formed IS NOT NULL AND split IS NULL THEN EXTRACT(YEAR FROM CURRENT_DATE()) - formed
          ELSE NULL
       END AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan;
