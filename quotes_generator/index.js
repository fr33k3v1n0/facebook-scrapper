//variables
// notre tableau de citations
// le tableau de citations est compose des citations qui sont eux aussi des tableau composer de la citation et de l'autheur
const quotes = [
    [
        "Un programme informatique fait ce que vous lui avez dit de faire,\
         pas ce que vous voulez qu'il fasse.",
        " loi de Greer de Loi de Murphy"

    ],
    [
        "Un siècle est proche de l'infini, Jorge, tant en informatique fondamentale\
        qu'en recherche biologique.",
        "Jean-Michel Calvez"
    ],
    [
        "Nous autres, mordus d'informatique, préférons par-dessus\
         tout passer notre temps à bidouiller nos ordinateurs\
         plutôt que les utiliser pour faire quelque chose de productif.",
         "Proffgims"
    ],
    [
        "En informatique, les invariants sont éphémères.",
        "Alain Rey"
    ],
    [
        "Quand on ne peut revenir en arrière, on ne doit se préoccuper que de la meilleure façon d'aller de l'avant",
        "Paulo Coelho"
    ],
    ["On ne tire pas sur une fleur pour la faire pousser. On l'arrose et on la regarde grandir... patiemment.", "proverbe Africain"]
    
];
quote_index = 0; //index de la citation a afficher
let quote_elem = document.querySelector('blockquote[class="quote"]'); // l'element html qui affiche la citation
author = document.getElementById('author'); // l'element html qui affiche l'autheur de la citationo
next_button = document.querySelector("button[class='button generate']") // le bounton pour generer un nouvelle citation

//useful functions
function changeText(element, text) {
    element.innerText = text
}
// quand l'utilisateur click sur le bouton nouveau, nous allons generer une nouvelle citation
changeText(quote_elem, quotes[quote_index][0]);
changeText(author, "PAR: "  + quotes[quote_index][1]);
next_button.addEventListener('click', 
()=>{
    old_index = quote_index
    while( quote_index == old_index) {
       // nous voulons une nouvelle citation defferente de la precedante 
        quote_index = Math.round(Math.random() * (quotes.length))
    }
    changeText(quote_elem, quotes[quote_index][0]);
    changeText(author, "PAR: "  + quotes[quote_index][1]);

}
)