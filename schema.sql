
--Once init_db has been called, to make changes:

-- edit the SCHEMA (model)
-- edit the CREATE_DB (controller)
-- edit the DISPLAY (view)

--the SCHEMA tells us what goes into a post
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, --each database should have a primary key!
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- we default to the current time,
    -- but we can also specify a time (for example when importing posts)
    title TEXT NOT NULL,
    content TEXT NOT NULL
);