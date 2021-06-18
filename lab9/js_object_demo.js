// this is object in JS, note that we use the dot notation to access properties values
todos = {
	"todos":[
		{
			"title":"Learn Pytohn",
			"completed": false,
			"userName": "Maria"
		},
		{
			"title":"Learn Mongodb",
			"completed": false,
			"userName":"Pesho"
		},
		{
			"title":"Learn Django",
			"completed": true
		}
	]
}

// in python dict:
// print( todos["todos"][0]["title"] );
console.log( todos.todos[0].title);