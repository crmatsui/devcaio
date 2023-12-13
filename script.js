let currentPageUrl = 'https://swapi.dev/api/people/'

window.onload = async () => {
    try{
        await loadCharacters(currentPageUrl);
    }   catch (error) {
        console.log(error);
        alert('Erro ao carregar cards');
    }

    const nextButton = document.getElementById('next-button')
    const backButton = document.getElementById('back-button')

    nextButton.addEventListener('click', loadNextPage)
    backButton.addEventListener('click', loadPreviousPage)

};

async function loadCharacters(url) {
    const mainContent = document.getElementById('main-content')
    mainContent.innerHTML = ''; // limpar os resultados interiores no caso cards da pagina 1. Para gerar somente cards da pagina 2.

        try {

            const response = await fetch(url);
            const responseJson = await response.json();

            responseJson.results.forEach((character) => {
                const cards = document.createElement("div")
                cards.style.backgroundImage = 
                `url('https://starwars-visualguide.com/assets/img/characters/${character.url.replace(/\D/g, "")}.jpg')`
                cards.className = "cards"

                const characterNameBG = document.createElement("div")
                characterNameBG.className = "character-name-bg"

                const characterName = document.createElement("span")
                characterName.className = "character-name"
                characterName.innerText = `${character.name}`

                characterNameBG.appendChild(characterName)
                cards.appendChild(characterNameBG)

                cards.onclick = () => {
                    const modal = document.getElementById("modal")
                    modal.style.visibility = "visible"

                    const modalContent = document.getElementById("modal-content")
                    modalContent.innerHTML = ''

                    const characterImage = document.createElement("div")
                    characterImage.style.backgroundImagem = 
                    `url('https://starwars-visualguide.com/assets/img/characters/${character.url.replace(/\D/g, "")}.jpg')`
                    characterImage.className = "character-Image"

                    const name = document.createElement("span")
                    name.className = "character-details"
                    name.innerText = 'Nome: ${character.name}'

                    const characterHeight = document.createElement("span")
                    characterHeight.className = "character-details"
                    characterHeight.innerText = 'Altura: ${character.height}'

                    const charactermass = document.createElement("span")
                    mass.className = "character-details"
                    mass.innerText = 'Peso: ${character.mass}'

                    const eyeColor= document.createElement("span")
                    eyeColor.className = "character-details"
                    eyeColor.innerText = 'Cor dos olhos: ${character.eyeColor}'

                    const birth_year= document.createElement("span")
                    birth_year.className = "character-details"
                    birth_year.innerText = 'Nascimento: ${character.birth_year}'

                    modalContent.appendChild(characterImage)
                    modalContent.appendChild(name)
                    modalContent.appendChild(characterHeight)
                    modalContent.appendChild(charactermass)
                    modalContent.appendChild(charactereyeColor)
                    modalContent.appendChild(characterbirthyear)
                }

                mainContent.appendChild(cards)
            });

            const nextButton = document.getElementById('next-button')
            const backButton = document.getElementById('back-button')

            nextButton.disabled = !responseJson.next
            backButton.disabled = !responseJson.previous

            backButton.style.visibility = responseJson.previous ? "visible" : "hidden"

            currentPageUrl = url

  } catch (error) {
  alert('Erro ao carregar os personagens')
  console.log(error)
  }
}

async function loadNextPage() {
    if (!currentPageUrl) return;

    try {
      const response = await fetch(currentPageUrl)
      const responseJson = await response.json()    

      await loadCharacters(responseJson.next)

    } catch (error) {
        console.log(error)        
        alert('Erro ao carregar a proxima pagina')
    }    
}
async function loadPreviousPage() {
    if (!currentPageUrl) return;
    
    try {
      const response = await fetch(currentPageUrl)
      const responseJson = await response.json()    
    
      await loadCharacters(responseJson.previous)
    
    } catch (error) {
      console.log(error)        
      alert('Erro ao carregar a pagina anterior')
    }    
}

function hideModal() {
    const modal = document.getElementById("modal")
    modal.style.visibility = "hidden"
}