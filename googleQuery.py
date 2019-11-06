import webbrowser

qID = 9

baseString = "https://wwww.google.com/search?query="
queryString = ""
if classPrediction[qID] == 0:
    queryString = "directions+to+Mexicani+near+me"
elif classPrediction[qID] == 1:
    queryString = "directions+to+Kapiot+near+me"
elif classPrediction[qID] == 2:
    queryString = "directions+to+karnaf+near+me"
else:
    webbrowser.open("https://www.brainstormil.com/projects")
urlString = baseString + queryString
webbrowser.open(urlString, new=2)