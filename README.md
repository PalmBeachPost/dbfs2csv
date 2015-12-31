What is this?
=============
This uses Python to bulk convert any DBF (dBase) files in a directory to CSV (comma-separated value) files, which play much nicer with modern database programs.

The only external dependency is the dbfread module. Install it like this:
`pip install dbfread`

This will work OK with the regular Python interpreter. But by using the alternate pypy interpreter (for which you'd separately have to install dbfread), you can triple your output. On modest hardware, this churned through a 1.1gb DBF file in less than 4 minutes, or about 5 megabytes/second.