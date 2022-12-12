CREATE DATABASE projeto_final_rec;

\q projeto_final_rec;

CREATE TABLE efluentes (
  id SERIAL NOT NULL PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  ph_emissao FLOAT NOT NULL,
  ph_permitido FLOAT NOT NULL,
  empresa VARCHAR(255) NOT NULL
);

INSERT INTO efluentes VALUES
  (DEFAULT, 'sólidos grosseiros em suspensão', 7.2, 6.5, 'MERCATRON'),
  (DEFAULT, 'sólidos em suspensão, sejam ou não sedimentáveis', 3, 5, 'MERCATRON'),
  (DEFAULT, 'graxas e óleos', 5, 5.1, 'MERCATRON'),
  (DEFAULT, 'metais pesados', 8.2, 7.5, 'MERCATRON'),
  (DEFAULT, 'matéria orgânica solúvel biodegradável', 9, 7, 'MERCATRON'),
  (DEFAULT, 'nitrogênio amoniacal', 5, 6.8, 'MERCATRON'),
  (DEFAULT, 'nitrato e nitrito', 2, 5, 'MERCATRON'),
  (DEFAULT, 'fósforo', 8, 7.7, 'MERCATRON'),
  (DEFAULT, 'matéria orgânica não biodegradável', 1, 3.2, 'MERCATRON'),
  (DEFAULT, 'toxicidade', 8, 8.2, 'MERCATRON'),
  (DEFAULT, 'sólidos grosseiros em suspensão', 7.2, 6.5, 'KEKREN'),
  (DEFAULT, 'sólidos em suspensão, sejam ou não sedimentáveis', 3, 5, 'KEKREN'),
  (DEFAULT, 'graxas e óleos', 5, 5.1, 'KEKREN'),
  (DEFAULT, 'metais pesados', 8.2, 7.5, 'KEKREN'),
  (DEFAULT, 'matéria orgânica solúvel biodegradável', 9, 7, 'KEKREN'),
  (DEFAULT, 'nitrogênio amoniacal', 5, 6.8, 'KEKREN'),
  (DEFAULT, 'nitrato e nitrito', 2, 5, 'KEKREN'),
  (DEFAULT, 'fósforo', 8, 7.7, 'KEKREN'),
  (DEFAULT, 'matéria orgânica não biodegradável', 1, 3.2, 'KEKREN'),
  (DEFAULT, 'toxicidade', 8, 8.2, 'KEKREN'),
  (DEFAULT, 'sólidos grosseiros em suspensão', 7.2, 6.5, 'LUSARTO'),
  (DEFAULT, 'sólidos em suspensão, sejam ou não sedimentáveis', 3, 5, 'LUSARTO'),
  (DEFAULT, 'graxas e óleos', 5, 5.1, 'LUSARTO'),
  (DEFAULT, 'metais pesados', 8.2, 7.5, 'LUSARTO'),
  (DEFAULT, 'matéria orgânica solúvel biodegradável', 9, 7, 'LUSARTO'),
  (DEFAULT, 'nitrogênio amoniacal', 5, 6.8, 'LUSARTO'),
  (DEFAULT, 'nitrato e nitrito', 2, 5, 'LUSARTO'),
  (DEFAULT, 'fósforo', 8, 7.7, 'LUSARTO'),
  (DEFAULT, 'matéria orgânica não biodegradável', 1, 3.2, 'LUSARTO'),
  (DEFAULT, 'toxicidade', 8, 8.2, 'LUSARTO');