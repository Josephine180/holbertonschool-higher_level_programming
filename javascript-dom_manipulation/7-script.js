fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
  const movieListe = document.getElementById('list_movies'); /* selection ul */
  data.results.forEach(movie => { /*on boucle sur les films */
    const li = document.createElement('li'); /* creation d'un element <li> */
    li.textContent = movie.title; /* ajout d'un film */
    movieListe.appendChild(li); /* ajouter à la liste */
  });
})
.catch(error => console.error('Erreur', error));