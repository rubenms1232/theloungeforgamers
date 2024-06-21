const gameContainer = document.getElementById("game-container");

fetch('games.json') 
  .then(response => response.json())
  .then(games => { 
    games.forEach(game => {
      const gameDiv = document.createElement("div");
      gameDiv.classList.add("game");

      gameDiv.innerHTML = `
        <a href="${game.game_url}" target="_blank"> <img src="${game.thumbnail}" alt="${game.title}"></a>
        <h2>${game.title}</h2>
        <p>Genre: ${game.genre}</p>
        <p>Platform: ${game.platform}</p>
        <p>${game.short_description}</p> 
        <a href="${game.freetogame_profile_url}" target="_blank">Learn More</a> 
      `;
      gameContainer.appendChild(gameDiv);
    });
  })
  .catch(error => {
    console.error("Error fetching data:", error);
    gameContainer.innerHTML = "<p>Error loading games.</p>"; 
  });