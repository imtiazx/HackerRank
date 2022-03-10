SELECT DISTINCT CITY
FROM STATION
WHERE UPPER(LEFT(CITY, 1)) NOT IN (
        'A'
        ,'E'
        ,'I'
        ,'O'
        ,'U'
        )
    OR LOWER(RIGHT(CITY, 1)) NOT IN (
        'a'
        ,'e'
        ,'i'
        ,'o'
        ,'u'
        );
