document.getElementById("add_item").addEventListener('click', function() {
const ul = document.querySelector(".my_list"); /* seletion ul element */
const li = document.createElement("li"); /* creation d'un nouveau <Li> element */
li.textContent = "Item"; /* attribuer du texte à l'element */
ul.appendChild(li); /* ajouter à ul */
});

