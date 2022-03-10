SELECT DISTINCT CITY
FROM STATION
WHERE UPPER(LEFT(CITY, 1)) NOT IN (
        'A'
        ,'E'
        ,'I'
        ,'O'
        ,'U'
        )
    AND LOWER(RIGHT(CITY, 1)) NOT IN (
        'a'
        ,'e'
        ,'i'
        ,'o'
        ,'u'
        );
