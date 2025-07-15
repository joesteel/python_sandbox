CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

INSERT INTO profiles (name, description)
VALUES
  ('Oprheus', 'likes music, bags of determination'),
  ('Eurdyuce', 'looking for love')
ON CONFLICT DO NOTHING;