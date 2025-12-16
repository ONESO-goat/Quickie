from pyscript import document



print("Hello world, From the web")
output_div = document.querySelector("#textarea")
output_div.innerText = "Hello World, From the web"