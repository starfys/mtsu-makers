<script type="text/javascript">



	//essentially the about page, might link to a more specific 'about' page
	var people = [
			{"firstName": "Stephen", "lastName":"Kinser", "github":"https://github.com/Riuchando"},
			{"firstName": "Kris", "lastName":"Brown", "github":"https://github.com/KrisB88"},
			{"firstName": "Steven", "lastName":"Sheffey", "github":"https://github.com/Starfys"}
			];
	
function peopletable(){
	
	//yay I can Javascript
	//essentially the about page, might link to a more specific 'about' page
	var people = [
			{"firstName": "Stephen", "lastName":"Kinser", "github":"https://github.com/Riuchando"},
			{"firstName": "Kris", "lastName":"Brown", "github":"https://github.com/KrisB88"},
			{"firstName": "Steven", "lastName":"Sheffey", "github":"https://github.com/Starfys"}
			];
	
	var out; //output to the webpage 
	
	out = "<h1>Contributors:</h1>" + "<table>"; // optional label
	 for (var i = 0 ; i< people.length; i++){	// go through every user put into a table
	out += 
	"<tr><td>" +people[i].firstName+"</td><td>"
			  +people[i].lastName+"</td><td>"
			  +"<a href=" + people[i].github+ "> github </a>" +"</td></tr>";
	} 
	out += "</table>";
	document.write(out)
}
</script>