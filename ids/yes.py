### From this playlist https://open.spotify.com/playlist/2WONKi3eZaR29QaQCRSiAE?si=337ecfa34ffe4f55
### It is mainly rap , and a bit of electro or rock
"""
Downloaded with this command in terminal :
curl -X "GET" "https://api.spotify.com/v1/playlists/2WONKi3eZaR29QaQCRSiAE/tracks?fields=items(track(id%2Cname))" 
-H "Accept: application/json" -H "Content-Type: application/json" 
-H "Authorization: Bearer [OAuth Token]" > yes.py  
"""

yes_ids = {
  "items" : [ {
    "track" : {
      "id" : "55mcupbf7cIsuCEVAuTJVk",
      "name" : "OVGTC - Star Wars remix"
    }
  }, {
    "track" : {
      "id" : "57RtLWT7IpugV0yi5bsxJk",
      "name" : "Rêves de môme"
    }
  }, {
    "track" : {
      "id" : "5VyfAfp2Yt3qaeuvq55ll3",
      "name" : "4 millions"
    }
  }, {
    "track" : {
      "id" : "3eWHY75nDgte70hh5yf4UW",
      "name" : "Bandana mauve"
    }
  }, {
    "track" : {
      "id" : "2UwrB6Ge6mPfUV8yGvAfX7",
      "name" : "Brothers (Remix Rilès)"
    }
  }, {
    "track" : {
      "id" : "4HolRqFuNvTvoLR2l1gexi",
      "name" : "Challenge incroyable #2"
    }
  }, {
    "track" : {
      "id" : "6dS1JCvtMJQ1O9bseVLyJz",
      "name" : "Freestyle Challenge"
    }
  }, {
    "track" : {
      "id" : "3zCWbPJVp1egCgyoMYAsDN",
      "name" : "Electron libérable"
    }
  }, {
    "track" : {
      "id" : "0O4U6fVE1TwWYhM4fKr1Fh",
      "name" : "WAW"
    }
  }, {
    "track" : {
      "id" : "3yFf0EtFwkiVSbf8CK4CB3",
      "name" : "EN ATTENDANT"
    }
  }, {
    "track" : {
      "id" : "4KMKVNmgBs8L2MMkJ3iDtG",
      "name" : "Bang Bang"
    }
  }, {
    "track" : {
      "id" : "2ODYKhD4xlPViKP4LrNAwD",
      "name" : "La marelle"
    }
  }, {
    "track" : {
      "id" : "6tQB8rJfdvILrxIxuKIRMu",
      "name" : "Christophe (Remix Orelsan)"
    }
  }, {
    "track" : {
      "id" : "4sTDuXa8uGDHwJdsXUqIBo",
      "name" : "Understood"
    }
  }, {
    "track" : {
      "id" : "4zHabeonyLGTgnR9R5RY3X",
      "name" : "Dimanche"
    }
  }, {
    "track" : {
      "id" : "2lTWOBGyQkBRIgzCtomXSL",
      "name" : "Depuis quand"
    }
  }, {
    "track" : {
      "id" : "3FVdWR0C2QAqXxhW1al2fT",
      "name" : "OUI"
    }
  }, {
    "track" : {
      "id" : "0V5c3isfSfyl7zQDtV9fAp",
      "name" : "Forever Broke"
    }
  }, {
    "track" : {
      "id" : "43kQu3PTBhCZCNhzaufAaX",
      "name" : "Two Tone Rebel"
    }
  }, {
    "track" : {
      "id" : "75bVc27bDSOAhMAL38cXpV",
      "name" : "Méchant"
    }
  }, {
    "track" : {
      "id" : "481uvgYccF51OUrEzIbop2",
      "name" : "Megazord"
    }
  }, {
    "track" : {
      "id" : "6mKLhdZIMaHpZ9kbmq9SOS",
      "name" : "Sankhara #4 (Chic)"
    }
  }, {
    "track" : {
      "id" : "0wSGClIhJMGkdamvWSTqX0",
      "name" : "Les 7 péchés capitaux / Colère"
    }
  }, {
    "track" : {
      "id" : "0gQB2HvjH14xfWVmYEUafn",
      "name" : "Siri 3"
    }
  }, {
    "track" : {
      "id" : "1zYBkCM626hfZmjIS1QYiX",
      "name" : "Le bon chemin"
    }
  }, {
    "track" : {
      "id" : "3UKwm5G898I1BvYt7uU4t0",
      "name" : "Petit con"
    }
  }, {
    "track" : {
      "id" : "0br27hgKNVMLyXKS3qjLOu",
      "name" : "Gaz"
    }
  }, {
    "track" : {
      "id" : "6u1rhQAvxkWLeuqUC3iJD0",
      "name" : "J'turn up (feat. Alkpote et Njd)"
    }
  }, {
    "track" : {
      "id" : "2MCAs3ttHSuDm1RHL0rqTF",
      "name" : "Jamais"
    }
  }, {
    "track" : {
      "id" : "7AJKmkPoSxic6mdUSjrbUZ",
      "name" : "Quoi de neuf?"
    }
  }, {
    "track" : {
      "id" : "3VYNqg6APRVQasDJnwlJ6H",
      "name" : "Féfé"
    }
  }, {
    "track" : {
      "id" : "4CF6itOplqlu7ilwLtYUl3",
      "name" : "Evil"
    }
  }, {
    "track" : {
      "id" : "59wSo3BVsBDZWMRKLwTpdv",
      "name" : "Tour de contrôle"
    }
  }, {
    "track" : {
      "id" : "07whpV2cnsEG3vk4qGxRQN",
      "name" : "Challenge incroyable"
    }
  }, {
    "track" : {
      "id" : "2HhCeucatmy92kC1NHJYjQ",
      "name" : "Legends Never Die"
    }
  }, {
    "track" : {
      "id" : "4gohbLz14XeqPbH5uxbZBz",
      "name" : "PIMP"
    }
  }, {
    "track" : {
      "id" : "35tyQCmxn6cj2r7eAb4JXP",
      "name" : "Carrépisode #3"
    }
  }, {
    "track" : {
      "id" : "3Sd7FiZtfsVHKEvjshCsHC",
      "name" : "Koro"
    }
  }, {
    "track" : {
      "id" : "6yE734jgKBYFAzymZ6Elal",
      "name" : "Gamme"
    }
  }, {
    "track" : {
      "id" : "0De4Cl3YncrwWkqJiJfA7k",
      "name" : "PLM"
    }
  }, {
    "track" : {
      "id" : "5mA2JwcgMq4FIIBKKKLsuW",
      "name" : "Lost"
    }
  }, {
    "track" : {
      "id" : "0E2IUIi4k7klypQqmEcrkt",
      "name" : "Double Face"
    }
  }, {
    "track" : {
      "id" : "27x1z3kAL3Jx5TF4HyikPG",
      "name" : "07 56 89 24 89"
    }
  }, {
    "track" : {
      "id" : "5UcJfhiAQOqC5MtpwsM20t",
      "name" : "Fuegolando (Kikesa Remix)"
    }
  }, {
    "track" : {
      "id" : "4VdQCcXDuzb6Ks1yLT9FnO",
      "name" : "Ceci n'est pas du rap (feat. Niro)"
    }
  }, {
    "track" : {
      "id" : "4uq48sO2YTTJ0l74R9tOdo",
      "name" : "Mort de rire"
    }
  }, {
    "track" : {
      "id" : "1UvYiDcJVolpUAQWpwrxNw",
      "name" : "Goulag"
    }
  }, {
    "track" : {
      "id" : "0HkoTr9t0f6MeqGoUS3E3e",
      "name" : "JOKER"
    }
  }, {
    "track" : {
      "id" : "6mkAhxAj1y5zvXWefkd9y7",
      "name" : "Toujours en retard"
    }
  }, {
    "track" : {
      "id" : "3a1kMFVGEPa0dykTF9Sv9m",
      "name" : "Style libre"
    }
  }, {
    "track" : {
      "id" : "4Y4diRGOGDxZcDh9qYwFVv",
      "name" : "230 (feat. PLK)"
    }
  }, {
    "track" : {
      "id" : "1rssdvnvf0DZ4s2jdB3DCT",
      "name" : "RVRE"
    }
  }, {
    "track" : {
      "id" : "5HIaPHHvXP9D7lcDdFlvf9",
      "name" : "Perle Rare"
    }
  }, {
    "track" : {
      "id" : "216QmkNpU3hIjeZtGocb9B",
      "name" : "On sait jamais (feat. Niska)"
    }
  }, {
    "track" : {
      "id" : "205HNJ73cgpC0LAOnuQiWT",
      "name" : "Bande organisée"
    }
  }, {
    "track" : {
      "id" : "0jU7JpfPrm7jjaLjFLXZLh",
      "name" : "T’as Compris L’Truc ?"
    }
  }, {
    "track" : {
      "id" : "6Fn1k9ctMXsh5xrrMRaGQZ",
      "name" : "Matrice"
    }
  }, {
    "track" : {
      "id" : "1NW4kNeeaRl5xxOnOLsYIJ",
      "name" : "Pareil"
    }
  }, {
    "track" : {
      "id" : "4W1RGS4ncIY1yrz38rysN3",
      "name" : "Pistolet Rose 2 - A COLORS SHOW"
    }
  }, {
    "track" : {
      "id" : "1LWunyq4LMbOGjPD128dJy",
      "name" : "Seul"
    }
  }, {
    "track" : {
      "id" : "4avTQmRrg717z7AuXqYY0V",
      "name" : "Bon déjà"
    }
  }, {
    "track" : {
      "id" : "3Abk2vuXSoz1z9lJKjJkCr",
      "name" : "SPEEDBOAT"
    }
  }, {
    "track" : {
      "id" : "6pjtY9QtWHxTqPkTfGW0ru",
      "name" : "Nouveaux Hippies, Pt. 3"
    }
  }, {
    "track" : {
      "id" : "5wXJNvoVOZBmB9b4EDP8xW",
      "name" : "Paye"
    }
  }, {
    "track" : {
      "id" : "136fhifxcZQYs60Qgac9bm",
      "name" : "Loin"
    }
  }, {
    "track" : {
      "id" : "0rs6jxe3647mGSc7l18Cq8",
      "name" : "Potentiel (feat. Orelsan)"
    }
  }, {
    "track" : {
      "id" : "0hkXsgdRk1TAOuOEpzznkI",
      "name" : "Rivage"
    }
  }, {
    "track" : {
      "id" : "5T5mtNBCvVQ01WPr3MRzUY",
      "name" : "Sang-froid"
    }
  }, {
    "track" : {
      "id" : "2fl01uGwbppFEci7qij1lU",
      "name" : "Y'a R"
    }
  }, {
    "track" : {
      "id" : "5fEJDiHWMECUifmNipjvqO",
      "name" : "BBJTM"
    }
  }, {
    "track" : {
      "id" : "51SASYrlAU3DByPIsQFT9B",
      "name" : "S.A.M.Y"
    }
  }, {
    "track" : {
      "id" : "03JjVo4OYciAi88SEdtDii",
      "name" : "S'en tirer"
    }
  }, {
    "track" : {
      "id" : "73csFz02rFRAGhlV7wFajY",
      "name" : "GROSSE BLETA (feat. Kaaris)"
    }
  }, {
    "track" : {
      "id" : "3Wy1HGyh2hnHMF0xS2tJqH",
      "name" : "Freestyle Savies #3"
    }
  }, {
    "track" : {
      "id" : "3ZkkwW0R78PahonxsdNZ4U",
      "name" : "Gris"
    }
  }, {
    "track" : {
      "id" : "1l4RFBJ96hKYXRBl9AWCVt",
      "name" : "Fais-le"
    }
  }, {
    "track" : {
      "id" : "063QMlz0AK9iDJmVZEc2fP",
      "name" : "Ailleurs"
    }
  }, {
    "track" : {
      "id" : "5hlashYN7IwHpQ4PLtQNf4",
      "name" : "Batman"
    }
  }, {
    "track" : {
      "id" : "3wG9ykVbw7fhfLsoZGPT1E",
      "name" : "Bleu pâle"
    }
  }, {
    "track" : {
      "id" : "1O4qKxSYi8Hs2nQEXrISZ4",
      "name" : "Windsor - A COLORS SHOW"
    }
  }, {
    "track" : {
      "id" : "5JIeLpAbKtpFrCSWeOAiwo",
      "name" : "Siri 4"
    }
  }, {
    "track" : {
      "id" : "7tN7t8ECFVrExNd3qaqT3u",
      "name" : "J'ai prié"
    }
  }, {
    "track" : {
      "id" : "2EMTOyiYWGOIS3qg5jkcQT",
      "name" : "Larmes"
    }
  }, {
    "track" : {
      "id" : "6KigD0mlF4VGDYiSEzAyYw",
      "name" : "Fight Back"
    }
  }, {
    "track" : {
      "id" : "66ks5ll4gswiaE7lfb2QMz",
      "name" : "Chloroquine"
    }
  }, {
    "track" : {
      "id" : "7gi31ULI4vzNFUw8pokrfm",
      "name" : "Dans l'dos"
    }
  }, {
    "track" : {
      "id" : "7Khbx8MgVTwIJe8YBi8tci",
      "name" : "No Stress"
    }
  }, {
    "track" : {
      "id" : "2o7n4nINXpjbo9VpsHZ8Ik",
      "name" : "Gang (feat. Kalash Criminel)"
    }
  }, {
    "track" : {
      "id" : "4QMaRC93F0aFx3S648CLyh",
      "name" : "Animal In Me"
    }
  }, {
    "track" : {
      "id" : "0PieJw6d3jyki3JTxgZhIr",
      "name" : "Watcher"
    }
  }, {
    "track" : {
      "id" : "3F1vWVOvzgKx7r5ZRp19gu",
      "name" : "Stress of Success"
    }
  }, {
    "track" : {
      "id" : "2UREu1Y8CO4jXkbvqAtP7g",
      "name" : "Monster"
    }
  }, {
    "track" : {
      "id" : "0i8JFpqe9cKwnrcvoNgl1L",
      "name" : "Feel Invincible"
    }
  }, {
    "track" : {
      "id" : "5O9Dz0h08LuBi0aVvDcylh",
      "name" : "The Resistance"
    }
  }, {
    "track" : {
      "id" : "4Ahphc0UzRSoMpJRHgnGQK",
      "name" : "I Want to Live"
    }
  }, {
    "track" : {
      "id" : "3dl4lXWlOxnGo94OqNtpdq",
      "name" : "Mauvais"
    }
  }, {
    "track" : {
      "id" : "3DWDcsDoXRIFynCREIkibM",
      "name" : "En première page"
    }
  }, {
    "track" : {
      "id" : "6fmtZEUoGwxPNvUgr0NJm1",
      "name" : "Bi Chwiya"
    }
  }, {
    "track" : {
      "id" : "2edc1m7WXxdBA61WlxSInp",
      "name" : "Derniers réglages"
    }
  }, {
    "track" : {
      "id" : "3qjDXaWCalJ9ZzaHBG4j3V",
      "name" : "Remise en forme"
    }
  } ]
}