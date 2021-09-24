const button = document.createElement("button")
button.innerText = "Click me"
document.body.appendChild(button)

button.addEventListener("click", function () {
	document.body.style.backgroundColor = "#99F"
})