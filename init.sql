DO
$$
    BEGIN
        CREATE TABLE IF NOT EXISTS student_performance
        (
            school     TEXT,
            sex        VARCHAR(1),
            age        INTEGER,
            address    VARCHAR(1),
            famsize    VARCHAR(3),
            pstatus    VARCHAR(1),
            medu       INTEGER,
            fedu       INTEGER,
            mjob       TEXT,
            fjob       TEXT,
            reason     TEXT,
            guardian   TEXT,
            traveltime INTEGER,
            studytime  INTEGER,
            failures   INTEGER,
            schoolsup  VARCHAR(3),
            famsup     VARCHAR(3),
            paid       VARCHAR(3),
            activities VARCHAR(3),
            nursery    VARCHAR(3),
            higher     VARCHAR(3),
            internet   VARCHAR(3),
            romantic   VARCHAR(3),
            famrel     INTEGER,
            freetime   INTEGER,
            goout      INTEGER,
            dalc       INTEGER,
            walc       INTEGER,
            health     INTEGER,
            absences   INTEGER,
            G1         INTEGER,
            G2         INTEGER,
            G3         INTEGER
        );
        CREATE TABLE IF NOT EXISTS import_job
        (
            file_name      TEXT,
            success        BOOLEAN,
            error_message  TEXT,
            all_null_count INTEGER,
            import_time    TIMESTAMP
        );
    END
$$;


