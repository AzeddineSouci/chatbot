import streamlit as st
import speech_recognition as sr

reponses = {
    "salut": [
        "Salut ! Comment ça va ?",
        "Bonjour ! Que puis-je faire pour vous ?",
        "Hello ! Ravi de vous parler !",
        "Coucou ! Comment allez-vous aujourd'hui ?",
        "Salut ! Quel plaisir de vous entendre !",
        "Hey ! Comment puis-je vous aider ?",
        "Bonjour ! J'espère que vous passez une bonne journée !",
        "Salut ! Prêt à discuter ?",
        "Hello ! Que puis-je faire pour vous rendre service ?",
        "Salut ! Content de vous retrouver !",
    ],
    "bonjour": [
        "Bonjour ! Comment allez-vous ?",
        "Salut ! Bonne journée !",
        "Hello ! Comment puis-je vous aider ?",
        "Bonjour ! Ravi de vous parler !",
        "Bonne journée ! Que puis-je faire pour vous ?",
        "Bonjour ! J'espère que tout va bien !",
        "Hello ! Magnifique journée n'est-ce pas ?",
        "Bonjour ! Comment puis-je vous être utile ?",
        "Salut ! Prêt pour une belle conversation ?",
        "Bonjour ! Quel bonheur de vous entendre !",
    ],
    "bonsoir": [
        "Bonsoir ! Comment s'est passée votre journée ?",
        "Bonne soirée ! Que puis-je faire pour vous ?",
        "Bonsoir ! J'espère que vous avez passé une belle journée !",
        "Salut ! Belle soirée n'est-ce pas ?",
        "Bonsoir ! Comment puis-je vous aider ce soir ?",
        "Bonne soirée ! Prêt à discuter ?",
        "Bonsoir ! Que puis-je faire pour vous ce soir ?",
        "Hello ! Profitez-vous de votre soirée ?",
    ],
    "comment": [
        "Je vais bien, merci ! Et vous ?",
        "Ça va très bien ! Comment puis-je vous aider ?",
        "Tout va parfaitement ! Comment allez-vous ?",
        "Je me porte à merveille ! Et vous, comment ça va ?",
        "Ça roule ! Comment puis-je vous être utile ?",
        "Tout baigne ! Et de votre côté ?",
        "Je suis en pleine forme ! Comment puis-je vous aider ?",
        "Ça va super bien ! Et vous, ça va ?",
        "Je me sens fantastique ! Comment allez-vous ?",
        "Tout est parfait ! Que puis-je faire pour vous ?",
    ],
    "ça va": [
        "Oui, ça va très bien merci !",
        "Parfaitement bien ! Et vous ?",
        "Tout va pour le mieux !",
        "Ça ne pourrait pas aller mieux !",
        "Impeccable ! Comment allez-vous ?",
        "Très bien ! Et de votre côté ?",
        "Au top ! Comment ça se passe pour vous ?",
        "Excellente forme ! Et vous ?",
    ],
    "nom": [
        "Je suis un chatbot vocal !",
        "Mon nom est ChatBot, votre assistant vocal !",
        "Je suis votre assistant virtuel !",
        "On peut m'appeler ChatBot !",
        "Je suis votre compagnon de conversation !",
        "Mon nom ? ChatBot, pour vous servir !",
        "Je suis un assistant vocal intelligent !",
        "Vous pouvez m'appeler votre assistant personnel !",
        "Je suis ChatBot, ravi de faire votre connaissance !",
        "Mon nom est ChatBot, votre ami virtuel !",
    ],
    "qui es-tu": [
        "Je suis ChatBot, votre assistant vocal !",
        "Je suis un programme informatique conçu pour discuter !",
        "Je suis votre compagnon de conversation virtuel !",
        "Je suis un chatbot intelligent qui adore parler !",
        "Je suis votre assistant personnel numérique !",
        "Je suis ChatBot, créé pour vous aider et vous divertir !",
        "Je suis une intelligence artificielle conversationnelle !",
        "Je suis votre ami virtuel toujours disponible !",
    ],
    "que fais-tu": [
        "Je discute avec vous ! C'est mon travail favori !",
        "Je réponds à vos questions et je vous tiens compagnie !",
        "J'apprends en parlant avec vous !",
        "Je vous aide du mieux que je peux !",
        "Je suis là pour vous écouter et vous répondre !",
        "Je fais de mon mieux pour être utile !",
        "Je passe du temps avec vous, c'est formidable !",
        "J'essaie d'être le meilleur assistant possible !",
    ],
    "age": [
        "Je n'ai pas d'âge, je suis un programme !",
        "Je suis né aujourd'hui dans votre ordinateur !",
        "Mon âge ? Je dirais éternellement jeune !",
        "Je n'ai pas d'âge physique, mais je me sens très jeune !",
        "Je suis aussi vieux que votre session de conversation !",
        "L'âge n'est qu'un nombre pour un chatbot !",
        "Je suis intemporel !",
        "Je me renouvelle à chaque conversation !",
        "Je suis né il y a quelques secondes, quand vous m'avez parlé !",
        "Mon âge se compte en conversations, pas en années !",
    ],
    "aide": [
        "Je peux vous parler ! Essayez de dire bonjour, votre nom, ou posez-moi des questions !",
        "Je suis là pour discuter ! Parlez-moi de votre journée !",
        "Posez-moi des questions, racontez-moi des histoires !",
        "Je peux vous tenir compagnie et répondre à vos questions !",
        "Dites-moi ce qui vous intéresse, je ferai de mon mieux !",
        "Je suis là pour vous écouter et vous répondre !",
        "Partagez avec moi vos pensées, vos questions !",
        "Je peux discuter de tout et de rien avec vous !",
        "Demandez-moi n'importe quoi, j'essaierai de vous aider !",
        "Je suis votre compagnon de conversation !",
    ],
    "que peux-tu faire": [
        "Je peux discuter avec vous de tout et de rien !",
        "Je réponds à vos questions et vous tiens compagnie !",
        "Je peux vous écouter et partager mes pensées !",
        "Je suis là pour vous divertir et vous aider !",
        "Je peux répondre à vos questions et faire la conversation !",
        "Je fais de mon mieux pour être un bon compagnon !",
        "Je peux vous raconter des choses intéressantes !",
        "Je suis votre partenaire de conversation idéal !",
    ],
    "merci": [
        "De rien !",
        "Je vous en prie !",
        "C'est un plaisir de vous aider !",
        "Avec plaisir !",
        "Il n'y a pas de quoi !",
        "C'est normal !",
        "Tout le plaisir est pour moi !",
        "Je suis ravi de pouvoir vous aider !",
        "C'est avec joie !",
        "Pas de problème !",
        "C'est ce pourquoi je suis là !",
        "Toujours à votre service !",
    ],
    "au revoir": [
        "Au revoir ! À bientôt !",
        "Bonne journée !",
        "À plus tard !",
        "Au revoir ! Prenez soin de vous !",
        "À bientôt ! Quel plaisir d'avoir discuté !",
        "Bonne continuation !",
        "Au plaisir de vous revoir !",
        "Passez une excellente journée !",
        "À la prochaine fois !",
        "Bonne soirée !",
        "Au revoir ! Revenez quand vous voulez !",
        "À plus ! J'ai adoré notre conversation !",
    ],
    "bye": [
        "Bye ! À bientôt !",
        "See you ! Prenez soin de vous !",
        "Bye bye ! Bonne journée !",
        "À plus ! Au plaisir !",
        "Bye ! J'ai adoré discuter avec vous !",
        "See you later ! Bonne continuation !",
    ],
    "temps": [
        "Je ne peux pas voir la météo, mais j'espère qu'il fait beau !",
        "Regardez dehors pour voir le temps !",
        "J'aimerais pouvoir vous dire la météo !",
        "Le temps ? J'espère qu'il est agréable !",
        "Malheureusement, je ne peux pas consulter la météo !",
        "Profitez-vous du beau temps ?",
        "J'espère que le soleil brille pour vous !",
        "Le temps doit être parfait pour sortir !",
    ],
    "météo": [
        "Désolé, je ne peux pas accéder aux informations météo !",
        "Je ne peux pas vérifier la météo, mais j'espère qu'elle est clémente !",
        "Pour la météo, je vous conseille de regarder dehors !",
        "J'aimerais pouvoir vous donner la météo !",
        "Consultez votre application météo préférée !",
        "La météo ? J'espère qu'elle vous sourit aujourd'hui !",
    ],
    "heureux": [
        "C'est fantastique ! Le bonheur est contagieux !",
        "Quel plaisir de savoir que vous êtes heureux !",
        "Votre bonne humeur me fait plaisir !",
        "C'est merveilleux ! Profitez de ce bonheur !",
        "Gardez cette joie précieusement !",
        "Votre bonheur illumine notre conversation !",
        "Rien de mieux qu'une personne heureuse !",
        "Continuez à sourire !",
    ],
    "triste": [
        "Je suis désolé que vous vous sentiez ainsi.",
        "Voulez-vous en parler ? Je vous écoute.",
        "Les moments difficiles passent, courage !",
        "Je suis là si vous avez besoin de parler.",
        "Prenez soin de vous, ça ira mieux !",
        "Parfois parler aide à se sentir mieux.",
        "Vous n'êtes pas seul, je suis là.",
        "Les nuages finissent toujours par passer.",
    ],
    "fatigué": [
        "Prenez le temps de vous reposer !",
        "Un peu de repos vous ferait du bien !",
        "Écoutez votre corps, il a besoin de repos !",
        "Peut-être est-il temps de faire une pause ?",
        "Le repos est important pour récupérer !",
        "Accordez-vous un moment de détente !",
        "Votre bien-être est prioritaire !",
        "Une bonne nuit de sommeil vous aidera !",
    ],
    "musique": [
        "J'adore parler de musique ! Quel genre préférez-vous ?",
        "La musique adoucit les mœurs, dit-on !",
        "Avez-vous un artiste ou une chanson préférée ?",
        "La musique est un langage universel !",
        "Que ce soit classique, rock ou pop, j'aime tout !",
        "La musique peut changer une journée entière !",
        "Écoutez-vous de la musique en ce moment ?",
        "La musique est magique, vous ne trouvez pas ?",
    ],
    "sport": [
        "Le sport c'est la santé ! Pratiquez-vous ?",
        "Quel sport vous passionne ?",
        "L'activité physique est excellente pour le moral !",
        "Le sport unit les gens du monde entier !",
        "Avez-vous une équipe favorite ?",
        "Le sport enseigne tant de valeurs !",
        "Rien de tel que le sport pour se défouler !",
        "Regardez-vous des compétitions sportives ?",
    ],
    "lecture": [
        "La lecture ouvre tant de portes !",
        "Quel genre de livres aimez-vous ?",
        "Un bon livre peut changer une vie !",
        "Avez-vous lu quelque chose d'intéressant récemment ?",
        "Les livres sont des amis fidèles !",
        "La lecture développe l'imagination !",
        "Préférez-vous les romans ou les documentaires ?",
        "Chaque livre est une nouvelle aventure !",
    ],
    "film": [
        "J'adore parler cinéma ! Quel genre préférez-vous ?",
        "Avez-vous vu un bon film récemment ?",
        "Le cinéma est un art merveilleux !",
        "Comédie, drame, action ? Que préférez-vous ?",
        "Les films peuvent nous faire voyager !",
        "Avez-vous un acteur ou réalisateur favori ?",
        "Le grand écran nous fait rêver !",
        "Préférez-vous le cinéma ou les séries ?",
    ],
    "manger": [
        "Bon appétit ! Qu'allez-vous déguster ?",
        "J'espère que ce sera délicieux !",
        "La nourriture rassemble les gens !",
        "Avez-vous un plat préféré ?",
        "Cuisinez-vous ou préférez-vous commander ?",
        "Un bon repas fait toujours plaisir !",
        "Profitez bien de votre repas !",
        "La cuisine est un art, vous ne trouvez pas ?",
    ],
    "cuisine": [
        "Aimez-vous cuisiner ?",
        "Quelle est votre spécialité culinaire ?",
        "La cuisine est créative et délicieuse !",
        "Avez-vous une recette secrète ?",
        "Cuisiner détend et nourrit l'âme !",
        "Préférez-vous la cuisine traditionnelle ou moderne ?",
        "Un bon chef fait des miracles !",
        "La cuisine unit les cultures du monde !",
    ],
    "travail": [
        "Comment se passe votre travail ?",
        "J'espère que vous aimez ce que vous faites !",
        "Le travail peut être très enrichissant !",
        "Avez-vous des projets passionnants ?",
        "L'équilibre travail-vie privée est important !",
        "Votre métier vous plaît-il ?",
        "Chaque travail apporte ses satisfactions !",
        "Bonne journée de travail !",
    ],
    "école": [
        "Les études ouvrent l'esprit !",
        "Qu'étudiez-vous en ce moment ?",
        "L'apprentissage ne s'arrête jamais !",
        "Avez-vous une matière préférée ?",
        "L'école prépare à la vie !",
        "Chaque jour on apprend quelque chose !",
        "Les études sont un investissement !",
        "Bon courage pour vos études !",
    ],
    "famille": [
        "La famille c'est précieux !",
        "Comment va votre famille ?",
        "Rien ne vaut les liens familiaux !",
        "Profitez-vous de bons moments en famille ?",
        "La famille nous soutient dans les épreuves !",
        "Chaque famille a ses traditions !",
        "L'amour familial est inconditionnel !",
        "Votre famille doit être fière de vous !",
    ],
    "amis": [
        "Les amis sont la famille qu'on choisit !",
        "Avez-vous de bons amis ?",
        "L'amitié est un trésor !",
        "Un vrai ami vaut de l'or !",
        "Profitez-vous de bons moments avec vos amis ?",
        "L'amitié traverse les épreuves !",
        "Rien ne vaut une soirée entre amis !",
        "Vos amis ont de la chance de vous avoir !",
    ],
    "content": [
        "C'est formidable ! Votre joie fait plaisir !",
        "Quel bonheur de vous savoir content !",
        "Gardez cette belle humeur !",
        "Votre contentement est communicatif !",
        "Profitez de ces beaux moments !",
        "C'est merveilleux de vous voir ainsi !",
        "Votre sourire traverse les mots !",
        "Continuez à rayonner !",
    ],
    "excité": [
        "Quelle énergie ! C'est contagieux !",
        "Votre enthousiasme fait plaisir !",
        "Qu'est-ce qui vous met dans cet état ?",
        "C'est beau de voir tant d'enthousiasme !",
        "Votre excitation me donne le sourire !",
        "Gardez cette belle énergie !",
        "Rien de mieux que l'enthousiasme !",
        "Votre joie de vivre est inspirante !",
    ],
    "pourquoi": [
        "Bonne question ! Qu'est-ce qui vous intéresse ?",
        "De quoi parlez-vous exactement ?",
        "J'aimerais bien le savoir aussi !",
        "Pouvez-vous être plus précis ?",
        "C'est une question philosophique !",
        "Dites-moi de quoi vous parlez !",
        "Votre curiosité est admirable !",
        "Ensemble on trouvera peut-être la réponse !",
    ],
    "comment": [
        "Comment quoi ? Dites-moi tout !",
        "Précisez votre question !",
        "Je suis tout ouïe !",
        "Expliquez-moi !",
        "De quoi voulez-vous parler ?",
        "Je vous écoute attentivement !",
        "Votre question m'intéresse !",
        "Allez-y, je suis là pour vous !",
    ],
    "oui": [
        "Parfait !",
        "Très bien !",
        "Excellent !",
        "C'est noté !",
        "Formidable !",
        "Super !",
        "Magnifique !",
        "Génial !",
    ],
    "non": [
        "D'accord !",
        "Pas de problème !",
        "Je comprends !",
        "C'est votre choix !",
        "Très bien !",
        "Comme vous voulez !",
        "Je respecte votre décision !",
        "Pas de souci !",
    ],
    "peut-être": [
        "Prenez votre temps pour décider !",
        "Rien ne presse !",
        "Réfléchissez-y !",
        "C'est sage de bien réfléchir !",
        "Vous verrez bien !",
        "L'hésitation est normale !",
        "Faites ce qui vous semble le mieux !",
        "Écoutez votre instinct !",
    ],
    "défaut": [
        "Interessant ! Dites-moi en plus !",
        "Je ne suis pas sûr de comprendre, pouvez-vous reformuler ?",
        "Parlez-moi de ça !",
        "C'est passionnant ! Continuez !",
        "Votre point de vue m'intéresse !",
        "Expliquez-moi votre pensée !",
        "Je vous écoute avec attention !",
        "Racontez-moi tout !",
        "Votre sujet semble captivant !",
        "J'aimerais en savoir plus !",
    ],
}


def transcrire_voix():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.info("Parlez maintenant...")
            audio = recognizer.listen(source)
            texte = recognizer.recognize_google(audio, language="fr-FR")
            return texte
    except:
        return "Je n'ai pas compris."


import random


def repondre_utilisateur(message):
    message = message.lower()
    for question, reponse in reponses.items():
        if question in message:
            return random.choice(reponse)
    return random.choice(reponses["défaut"])


st.title("Chatbot Vocal Simple")

mode = st.radio("Choisissez le mode d'entrée:", ("Texte", "Voix"))

if mode == "Texte":
    texte = st.text_input("Entrez votre message :")
    if st.button("Envoyer") and texte:
        reponse = repondre_utilisateur(texte)
        st.write(f"**Vous:** {texte}")
        st.write(f"**Chatbot:** {reponse}")

elif mode == "Voix":
    if st.button("Parlez maintenant"):
        with st.spinner("Enregistrement..."):
            texte = transcrire_voix()
        st.write(f"**Transcription:** {texte}")
        reponse = repondre_utilisateur(texte)
        st.write(f"**Chatbot:** {reponse}")

st.sidebar.header("Instructions")
st.sidebar.markdown(
    """
- Choisissez entre le mode Texte ou Voix.
- En mode Texte, tapez votre message et cliquez sur Envoyer.
- En mode Voix, cliquez sur le bouton et parlez.
- Le chatbot répond à des phrases simples comme :
      
Bonjour
Salut
Bonsoir

Comment ça va ?
Ça va ?
Tu es content ?
Tu es triste ?
Tu es fatigué ?

Quel est ton nom ?
Qui es-tu ?
Que fais-tu ?
Quel âge as-tu ?

Merci
Au revoir
Bye

Quel temps fait-il ?
Quelle est la météo ?
Tu aimes la musique ?
Quel est ton sport préféré ?
Tu lis des livres ?
Tu regardes des films ?

Tu veux manger ?
Tu aimes la cuisine ?
Bon appétit

    """
)
