@echo off
setlocal EnableDelayedExpansion
set "search_term=neki"
set "output_file=save.txt"

echo Searching for "%search_term%" in all files...

(for /r %%F in (*) do (
    findstr /i /c:"%search_term%" "%%F" > nul && (
        for /f "delims=" %%L in ('findstr /n /i /c:"%search_term%" "%%F"') do (
            set "line=%%L"
            set "line=!line:*:=!"
            echo Found "%search_term%" in "%%F" (line !line!): !line_content!
            echo "!line_content!" >> "%output_file%"
        )
    )
)) > nul

echo Done. Results saved in "%output_file%".