import requests
import json
import os

def fetch_games():
    """Fetches game data from the API."""
    url = "https://www.freetogame.com/api/games?platform=pc"
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
<html lang="en">

  <head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap" rel="stylesheet">

    <title>The Lounge For Gamers</title>

    <!-- Bootstrap core CSS -->
    <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">


    <!-- Additional CSS Files -->
    <link rel="stylesheet" href="assets/css/fontawesome.css">
    <link rel="stylesheet" href="assets/css/temp.css">
    <link rel="stylesheet" href="assets/css/owl.css">
    <link rel="stylesheet" href="assets/css/animate.css">
    <link rel="stylesheet"href="https://unpkg.com/swiper@7/swiper-bundle.min.css"/>
<!--

-->
  </head>

<body>

  <!-- ***** Preloader Start ***** -->
  <div id="js-preloader" class="js-preloader">
    <div class="preloader-inner">
      <span class="dot"></span>
      <div class="dots">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </div>
  <!-- ***** Preloader End ***** -->

  <!-- ***** Header Area Start ***** -->
  <header class="header-area header-sticky">
    <div class="container">
        <div class="row">
            <div class="col-12">
                <nav class="main-nav">
                    <!-- ***** Logo Start ***** -->
                    <a href="index.html" class="logo">
                        <img src="assets/images/logo.png" alt="">
                    </a>
                    <!-- ***** Logo End ***** -->
                    <!-- ***** Search End ***** -->
                    <div class="search-input">
                      <form id="search" action="#">
                        <input type="text" placeholder="Type Something" id='searchText' name="searchKeyword" onkeypress="handle" />
                        <i class="fa fa-search"></i>
                      </form>
                    </div>
                    <!-- ***** Search End ***** -->
                    <!-- ***** Menu Start ***** -->
                    <ul class="nav">
                        <li><a href="index.html" >Home</a></li>
                        <li><a href="PCGAMES.html" class="active">PC Games</a></li>
                   <!-- <li><a href="browse.html">Browse</a></li>
                        <li><a href="details.html">Details</a></li>
                        <li><a href="streams.html">Streams</a></li>
                        <li><a href="profile.html">Profile <img src="assets/images/profile-header.jpg" alt=""></a></li>-->
                    </ul>   
                    <a class='menu-trigger'>
                        <span>Menu</span>
                    </a>
                    <!-- ***** Menu End ***** -->
                </nav>
            </div>
        </div>
    </div>
  </header>
  <!-- ***** Header Area End ***** -->

  <div class="container">
    <div class="row">
      <div class="col-lg-12">
        <div class="page-content">
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
              <h4><a href="{game['game_url']}" target="_blank">{game['title']}</a><br><span>{game['genre']}</span><span>{game['platform']}</span></h4>
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
                    <<h4><a href="{game['game_url']}" target="_blank">{game['title']}</a><br><span>{game['genre']}</span><span>{game['platform']}</span></h4>
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
              <h4><a href="{game['game_url']}" target="_blank">{game['title']}</a><br><span>{game['genre']}</span><span>{game['platform']}</span></h4>
              <ul>
                
              </ul>
            </div>
          </div>
        """
    html += """
                            <!--<div class="col-lg-12">
                    <div class="main-button">
                      <a href="browse.html">Discover Popular</a> </div>
                  </div>-->
                </div> 
              </div>
            </div>
          </div> 
          <script src="script.js"></script> 
        </body>
        </html>
            
        
          
</body>
</html>
    
          <!-- ***** Most Popular End ***** -->

          <!-- ***** Gaming Library Start ***** -->
         <!-- <div class="gaming-library">
            <div class="col-lg-12">
              <div class="heading-section">
                <h4><em>Your Gaming</em> Library</h4>
              </div>
              <div class="item">
                <ul>
                  <li><img src="assets/images/game-01.jpg" alt="" class="templatemo-item"></li>
                  <li><h4>Dota 2</h4><span>Sandbox</span></li>
                  <li><h4>Date Added</h4><span>24/08/2036</span></li>
                  <li><h4>Hours Played</h4><span>634 H 22 Mins</span></li>
                  <li><h4>Currently</h4><span>Downloaded</span></li>
                  <li><div class="main-border-button border-no-active"><a href="#">Donwloaded</a></div></li>
                </ul>
              </div>
              <div class="item">
                <ul>
                  <li><img src="assets/images/game-02.jpg" alt="" class="templatemo-item"></li>
                  <li><h4>Fortnite</h4><span>Sandbox</span></li>
                  <li><h4>Date Added</h4><span>22/06/2036</span></li>
                  <li><h4>Hours Played</h4><span>740 H 52 Mins</span></li>
                  <li><h4>Currently</h4><span>Downloaded</span></li>
                  <li><div class="main-border-button"><a href="#">Donwload</a></div></li>
                </ul>
              </div>
              <div class="item last-item">
                <ul>
                  <li><img src="assets/images/game-03.jpg" alt="" class="templatemo-item"></li>
                  <li><h4>CS-GO</h4><span>Sandbox</span></li>
                  <li><h4>Date Added</h4><span>21/04/2036</span></li>
                  <li><h4>Hours Played</h4><span>892 H 14 Mins</span></li>
                  <li><h4>Currently</h4><span>Downloaded</span></li>
                  <li><div class="main-border-button border-no-active"><a href="#">Donwloaded</a></div></li>
                </ul>
              </div>
            </div>
            <div class="col-lg-12">
              <div class="main-button">
                <a href="profile.html">View Your Library</a>
              </div>
            </div>
          </div>-->
          <!-- ***** Gaming Library End ***** -->
        </div>
      </div>
    </div>
  </div>
  
  <footer>
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <p>Copyright © 2024 <a href="#">Lounge For Gamers</a> Company. All rights reserved. 
          
        </div>
      </div>
    </div>
  </footer>


  <!-- Scripts -->
  <!-- Bootstrap core JavaScript -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.min.js"></script>

  <script src="assets/js/isotope.min.js"></script>
  <script src="assets/js/owl-carousel.js"></script>
  <script src="assets/js/tabs.js"></script>
  <script src="assets/js/popup.js"></script>
  <script src="assets/js/custom.js"></script>


  </body>

</html>
    """
    return html

if __name__ == "__main__":
    if not os.path.exists("images"):
        os.makedirs("images")

    games = fetch_games()
    html_content = generate_html(games)

    with open("pcgames_update.html", "w") as f:
        f.write(html_content)

    print("HTML file and images generated successfully!")