What is this?
=============
This uses Python to bulk convert any DBF (dBase) files in a directory to CSV (comma-separated value) files, which play much nicer with modern database programs.

This relies on external dependencies.

`pip install -r requirements.txt`

The Python 2 version was built for [one purpose]("https://source.opennews.org/articles/notes-working-big-ish-data/") and did well for that.

The Python 3 version fails on that original purpose, with an ["unpack error"](https://github.com/olemb/dbfread/issues/28) that's been present for more than a year in an underlying library. However, it seemed to work on three very small test files.

Using a pypy interpreter over stock Python might get you a substantial thoroughput increase.


Need something for Excel?
=========================
@dannguyen has a similar script for [XLSX files made by Excel](https://gist.github.com/dannguyen/d83f27a93b2e6f80edda22cfa0f0a1d6).

