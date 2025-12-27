SELECT
    id,
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat)
            THEN (SELECT student FROM Seat WHERE id = s.id + 1)
        WHEN id % 2 = 0
            THEN (SELECT student FROM Seat WHERE id = s.id - 1)
        ELSE student
    END AS student
FROM Seat s
ORDER BY id;