set wiki_URLs to {} -- creates a new list
set URLs to paragraphs of (read POSIX file "/users/emily/downloads/GeoURLsFinal.txt") --read file directory
repeat with nextLine in URLs
	if length of nextLine is greater than 0 then
		copy nextLine to the end of wiki_URLs --append each text file line URL to a list
	end if
end repeat

set the_URL_list to wiki_URLs as list --list URLs
set the list_count to the count of the_URL_list --gets number of items in the list
set pick to random number from 1 to list_count --chooses a random item from the list
set randomly_generated_url to item pick of the_URL_list as string --sets the generated item as the choice

set theAlertText to "Here is your new geo link of the day"
set theAlertMessage to randomly_generated_url --this is text within message box
display alert theAlertText ¬
	message theAlertMessage ¬
	as critical buttons {"Cancel", "Open Link"} ¬
	default button ¬
	"Open Link" cancel button "Cancel" giving up after 60 ¬
	
set the button_pressed to the button returned of the result
if the button_pressed is "Open Link" then --when "Open Link" is clicked the button goes to the random link. If "Cancel" is clicked nothing happens
	open location theAlertMessage
end if

return randomly_generated_url --displays one of the randomly chosen URLs in result box of appple script
