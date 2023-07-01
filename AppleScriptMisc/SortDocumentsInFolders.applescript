set sourceFolder to choose folder with prompt "Select the folder containing the files"

set destinationFolder to choose folder with prompt "Select the destination folder for organizing the files"

tell application "System Events"
    set fileNames to name of every file of folder sourceFolder
end tell

repeat with fileName in fileNames
    set AppleScript's text item delimiters to "."
    set fileExtension to last text item of fileName
    set AppleScript's text item delimiters to ""
    
    tell application "Finder"
        set destinationFolderPath to (destinationFolder as text) & fileExtension
        if not (exists folder destinationFolderPath) then
            make new folder at destinationFolder with properties {name:fileExtension}
        end if
    end tell
    
    tell application "Finder"
        set sourceFilePath to (sourceFolder as text) & fileName
        set destinationFilePath to destinationFolderPath & ":" & fileName
        move file sourceFilePath to folder destinationFolderPath
    end tell
end repeat

display notification "Operation Done" with title "Organize Files"
