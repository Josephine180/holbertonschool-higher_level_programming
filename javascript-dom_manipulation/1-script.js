// Sélectionne l'élément avec l'ID "red_header" et ajoute un écouteur d'événement
document.getElementById("red_header").addEventListener('click', function() {
  // récupérer id avec 'red_header'
  const header = document.getElementById("red_header");
  // changer la couleur chaque fois que l'élement est cliqué
  header.style.color = "#FF0000";
});