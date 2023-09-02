CREATE TABLE IF NOT EXISTS youtube(
id SERIAL PRIMARY KEY,
type TEXT,
title TEXT,
description TEXT,
videoId TEXT,
created_at DATE,
channel TEXT
);
