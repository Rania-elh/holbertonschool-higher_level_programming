fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        const listMovies = document.getElementById("list_movies");
        const movies = data.results;
        
        movies.forEach(function(movie) {
            const listItem = document.createElement("li");
            listItem.textContent = movie.title;
            listMovies.appendChild(listItem);
        });
    });
