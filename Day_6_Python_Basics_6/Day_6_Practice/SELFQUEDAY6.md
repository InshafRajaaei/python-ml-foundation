Self-Study Questions

1. Modes: What happens if you open a file in "w" mode that already has text in it? (Answer: It erases everything immediately).

2. Whitespace: When you use f.readline(), why does print(line) often output an extra blank line? (Answer: The file line has a hidden \n at the end, and print() adds another \n. Use .strip() to fix it).

2. OS: Why should you use pathlib or os.path.join instead of writing "folder/file.txt"? (Answer: Windows uses \ and Linux uses /. The modules handle this automatically).

4. Cursor: If I run f.read() and then immediately run f.read() again, what does the second one return? (Answer: Empty string "", because the cursor is at the end of the file. You must use f.seek(0) to reset).