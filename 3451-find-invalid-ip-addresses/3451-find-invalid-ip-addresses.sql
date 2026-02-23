SELECT
    ip,
    COUNT(*) AS invalid_count
FROM logs
WHERE
    -- Not exactly 3 dots (must have 4 octets)
    LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) != 3

    OR

    -- Non-numeric characters
    ip REGEXP '[^0-9.]'

    OR

    -- Any octet > 255
    CAST(SUBSTRING_INDEX(ip, '.', 1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS UNSIGNED) > 255
    OR CAST(SUBSTRING_INDEX(ip, '.', -1) AS UNSIGNED) > 255

    OR

    -- Leading zeros (except "0")
    ip REGEXP '(^|\\.)0[0-9]+'
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;