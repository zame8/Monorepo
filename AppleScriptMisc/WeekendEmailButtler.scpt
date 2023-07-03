tell application "Mail"
    activate
    
    set replySubject to "Re: {originalSubject}"
    set replyContent to "Hello {senderName}," & return & return & "Thank you for your email. Please note that it is currently the weekend, and I will get back to you on Monday." & return & return & "Best regards," & return & "Emaz"
    
    set currentDate to (current date)
    set currentWeekday to weekday of currentDate
    
    if currentWeekday is Saturday or currentWeekday is Sunday then
        set selectedMessages to selection
        repeat with theMessage in selectedMessages
            set originalSubject to subject of theMessage
            set senderName to name of sender of theMessage
            
            set replyMessage to reply theMessage with opening window
            set subject of replyMessage to replySubject
            set content of replyMessage to replyContent
        end repeat
    else
        display dialog "No new emails to reply to."
    end if
end tell
