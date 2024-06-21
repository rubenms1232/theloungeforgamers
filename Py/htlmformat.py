import requests
import json
import os

def fetch_games():
    """Fetches game data from the API."""
    url = "https://www.freetogame.com/api/games"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_and_save_image(image_url, filename):
    """Downloads an image and saves it to a file."""
    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, 'wb') as f:
        f.write(response.content)

def generate_html(games):
    """Generates HTML content matching the provided structure."""
    html = """
<!DOCTYPE html>
<html>
<head>
  <title>Awesome Games</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
 <div class="most-popular">
    <div class="row">
      <div class="col-lg-12">
        <div class="heading-section">
          <h4><em>Most Popular</em> Right Now</h4>
        </div>
        <div class="row">
    """

    # Displaying the games 
    for i in range(len(games)):
        game = games[i]
        image_filename = f"images/{game['id']}.jpg"
        download_and_save_image(game['thumbnail'], image_filename)
        if i < 4:
          html += f"""
          <div class="col-lg-3 col-sm-6">
            <div class="item">
              <img src="{image_filename}" alt="{game['title']}">
              <h4><a href="{game['game_url']}" target="_blank">{game['title']}</a><br><span>{game['genre']}</span></h4>
              <ul>
                
              </ul>
            </div>
          </div>
        """
        elif i == 4:
          html += """
          <div class="col-lg-6">
            <div class="item">
              <div class="row">
        """
        if 4 <= i < 6:
          html += f"""
                <div class="col-lg-6 col-sm-6">
                  <div class="item inner-item">
                    <img src="{image_filename}" alt="{game['title']}">
                    <h4><a href="{game['game_url']}" target="_blank">{game['title']}</a><br><span>{game['genre']}</span></h4>
                    <ul>
                      
                    </ul>
                  </div>
                </div>
            """
        if i == 5:
          html += """
              </div>
            </div>
          </div>
        """
        if i >= 6:
          html += f"""
          <div class="col-lg-3 col-sm-6">
            <div class="item">
              <img src="{image_filename}" alt="{game['title']}">
              <h4><a href="{game['game_url']}" target="_blank">{game['title']}</a><br><span>{game['genre']}</span></h4>
              <ul>
                
              </ul>
            </div>
          </div>
        """
    html += """
          <div class="col-lg-12">
            <div class="main-button">
              <a href="browse.html">Discover Popular</a> </div>
          </div>
        </div> 
      </div>
    </div>
  </div> 
  <script src="script.js"></script> 
</body>
</html>
    """
    return html

if __name__ == "__main__":
    if not os.path.exists("images"):
        os.makedirs("images")

    games = fetch_games()
    html_content = generate_html(games)

    with open("update.html", "w") as f:
        f.write(html_content)

    print("HTML file and images generated successfully!")