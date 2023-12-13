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
                    characterImage.style.backgroundImage = 
                    `url('https://starwars-visualguide.com/assets/img/characters/${character.url.replace(/\D/g, "")}.jpg')`
                    characterImage.className = "character-image"

                    const name = document.createElement("span")
                    name.className = "character-details"
                    name.innerText = `Nome: ${character.name}`

                    const height = document.createElement("span")
                    height.className = "character-details"
                    height.innerText = `Altura: ${convertHeight(character.height)}`

                    const mass = document.createElement("span")
                    mass.className = "character-details"
                    mass.innerText = `Peso: ${convertMass(character.mass)}`

                    const eye_color= document.createElement("span")
                    eye_color.className = "character-details"
                    eye_color.innerText = `Cor dos olhos: ${convertEyeColor(character.eye_color)}`
                   

                    const birth_year= document.createElement("span")
                    birth_year.className = "character-details"
                    birth_year.innerText = `Nascimento: ${convertBirthYear(character.birth_year)}`

                    modalContent.appendChild(characterImage)
                    modalContent.appendChild(name)
                    modalContent.appendChild(height)
                    modalContent.appendChild(mass)
                    modalContent.appendChild(eye_color)
                    modalContent.appendChild(birth_year)
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

function convertEyeColor(eye_color) {
    const cores = {
        blue: "azul",
        brown: "castanho",
        green: "verde",
        yellow: "amarelo",
        black: "preto",
        pink: "rosa",
        red: "vermelho",
        orange: "laranja",
        hazel: "avelã",
        unknown: "desconhecida"
    };

    return cores [eye_color.toLowerCase()] || eye_color;
}

function convertHeight(height) {
    if (height === "unknow") {
        return "desconhecida"
    }

    return (height / 100).toFixed(2);
}

function convertMass(mass) {
    if (mass === "unknown") {
        return "desconhecido"
    }

    return `${mass} kg`
}

function convertBirthYear(birth_year) {
    if (birth_year === "unknown") {
        return "desconhecido"
    }

    return birth_year
}