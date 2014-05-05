CREATE TABLE IF NOT EXISTS responses
(
  id serial NOT NULL,
  "order" character varying(255),
  CONSTRAINT responses_pkey PRIMARY KEY (id)
)
