@bottle.post("/favourite_fruit")
def favourite_fruit():
	fruit = bottle.request.forms.get("fruit")
	if (fruit==None or fruit == ""):
		fruit = "No fruit selected"
	return bottle.template("fruit_selection", {"fruit": fruit})


<form action="/favourite_fruit" action="POST">
What is your favourite route
<input type="text" name="fruit" size=40 value=""><br>
<input type="submit" value="Submit">
</form>
