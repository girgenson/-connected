import random

n = random.randint(10 ** 9, 10 ** 10)
type_of_entries = {1: 'person', 2: 'musician', 3: 'rapper', 4: 'actor', 5: 'article', 6: 'song', 7: 'track',
                   8: 'producer', 9: 'songwriter', 10: 'article', 11: 'movie_director', 12: 'online newspaper',
                   13: 'film', 14: 'animated film'}

entries = [

    {'id': n, 'name': 'Questlove', 'alias': '?love',
     'type': {type_of_entries[1], type_of_entries[2], type_of_entries[11], },
     'links': {n + 1, }
     },

    {'id': n + 1, 'name': 'Entertainment_News/TV/2022/03/29/Questlove-meditating-Oscar-Tonight-Show',
     'type': {type_of_entries[10], },
     'content':
         'March 29 (UPI) -- Ahmir "Questlove" Thompson said that he was unaware that Will '
         'Smith had slapped Chris Rock before he won his Oscar for Best Documentary Feature while appearing on The '
         'Tonight '
         'Show Starring Jimmy Fallon. '
         ''
         'Questlove, who is normally on the Tonight Show as a member of The Roots, sat down next to Fallon on Monday '
         'with his '
         'Oscar statue to talk about his big win and what happened right before he claimed his award. '
         ''
         'Questlove told Fallon that he was meditating before he won the award. Questlove won for his documentary '
         'feature '
         'Summer of Soul (... Or, When the Revolution Could Not Be Televised), which explores the 1969 Harlem Cultural '
         'Festival. '

         '"When the commercial break was happening I was just in my, \'Mmmmm.\' So when I opened my eyes, I didn\'t '
         'realize like, '
         '\'Why is everyone so quiet?\' Like I literally was not present for that whole entire moment," Questlove said '
         'about '
         'Smith slapping Rock for making a joke about his wife Jada Pinkett Smith. Rock then presented Best '
         'Documentary Feature '
         'to Questlove.'
         ''
         '"As I\'m walking to the stage, I\'m kind of putting two and two together and I realize that was a real '
         'moment like '
         'maybe three seconds before I spoke words. But in my mind, they were just doing a sketch or whatever and I\'m '
         'just '
         'like, \'Okay Ahmir. Remember to thank your mom, your dad.\' So I was not present at all. I was just in a '
         'blank space, '
         '" he continued.'
         ''
         'Fallon mentioned how he cried watching Questlove win. The filmmaker and musician then thanked Fallon for '
         'giving him a '
         'platform to chase his dreams at The Tonight Show and at NBC\'s 30 Rock studio. Questlove called 30 Rock the '
         'best '
         'college he\'s ever been to.'
         ''
         '"I didn\'t even start to listen to my dreams until I came here in 2009, so I really want to thank you for '
         'giving me '
         'that platform," Questlove said to Fallon before shaking his hand.',
     'links': (n, n + 2, n + 8)},

    {'id': n + 2, 'name': 'Will Smith', 'alias': 'Fresh Prince, Willard Carroll Smith II',
     'type': {type_of_entries[1], type_of_entries[2], type_of_entries[3], type_of_entries[4], },
     'content':
         'Willard Carroll "Will" Smith II (born September 25, 1968) is an American actor, comedian, producer, '
         'rapper, and songwriter. He has enjoyed success in television, film, and music. In April 2007, '
         'Newsweek called him "the most powerful actor in Hollywood".',
     'links': {n + 3, n, }
     },

    {
        'id': n + 3, 'name': 'Friend Like Me (End Title)', 'alias': 'Friend Like Me, End Title',
        'type': {type_of_entries[6], type_of_entries[7], },
        'release_year': '2019', 'producers': 'DJ Khaled, Danja, Ben Billions',
        'links': {n + 4, n + 2}
    },

    {'id': n + 4, 'name': 'Danja', 'alias': 'Floyd Nathaniel Hills', 'type': {type_of_entries[8], type_of_entries[9]},
     'links': {n + 5, n + 3, n + 7}
     },

    {'id': n + 5, 'name': 'Maneater (Remix)', 'alias': 'Nelly Furtado feat. Lil Wayne - Maneater (Remix)',
     'type': {type_of_entries[6], type_of_entries[7], }, 'links': {n + 4, n + 6}
     },

    {'id': n + 6, 'name': 'Nelly Furtado', 'alias': 'Nelly Kim Furtado, born December 2, 1978',
     'content':
         'Nelly Kim Furtado was born on December 2, 1978 in Victoria, British Columbia, Canada to Maria Manuela'
         'Furtado (née Neto), a motel cleaner & António José Furtado, a stonemason. She first gained fame with her '
         'trip hop inspired debut album, Whoa, Nelly! (2000), which was a critical and commercial success that spawned '
         'two top 10 singles on the Billboard Hot 100, I\'m Like a Bird and Turn Off the Light. The first of the two '
         'singles won her a Grammy Award for Best Female Pop Vocal Performance. Furtado\'s introspective folk-heavy '
         '2003 second album, Folklore, explored her Portuguese roots. Its singles received moderate success in Europe,'
         'but the album\'s underperformance compared to her debut was regarded as a sophomore slump.',
     'links': {n + 5, }
     },

    {'id': n + 7, 'name': 'Sober_(Pink_song)', 'links': {n + 4, n + 9}},

    {'id': n + 8, 'name': 'Jimmy Fallon', 'links': {n + 1, }},

    {
        'id': n + 9, 'name': 'Pink: The Truth About Love', 'type': {type_of_entries[10], },
        'content':
            '''Since approximately the turn of the millennium, Pink has been the most emotionally honest pop singer to 
     approach Top 40 radio on its own terms. (As opposed to Adele, who made Top 40 radio approach her on her terms.) 
     Think about her competition: Even when she’s allegedly opening up, does anybody think that “If I Were A Boy” or 
     “Irreplaceable” actually reveal anything about Beyoncé? But when Pink sings “Don’t Let Me Get Me,” “Sober,
     ” or even something as raucously anthemic as “So What,” it’s hard not to walk away with the feeling that she’s 
     giving her audience, well, her. 

     On The Truth About Love, Pink does the unthinkable: She starts to recede. Deliberately or otherwise, 
     she seems to shapeshift from track to track in order to ape the sound and style of any number of her 
     contemporaries. “Walk Of Shame” covers the same frivolous, wink-y ground as Katy Perry’s “Last Friday Night (
     T.G.I.F.)” in both sound and subject, while the guitar-heavy “Slut Like You” runs a Blur hook through a Lady 
     Gaga filter. (The tipsy spoken-word bridge is all Pink, though.) “How Come You’re Not Here?” and “Just Give Me A 
     Reason” suggest that Pink’s been listening to the Black Keys and Brandi Carlile, respectively, and a handful of 
     other songs sound as though they were produced in a panic the day after Kelly Clarkson’s Stronger came out.''',

        'links': {n + 10, n + 7}
    },

    {
        'id': n + 10, 'name': 'The_A.V._Club', 'type': {type_of_entries[12], },
        'links': {n + 9, n + 11}
    },

    {
        'id': n + 11, 'name': 'WALL-E', 'type': {type_of_entries[13], type_of_entries[14]},
        'content':
            '''WALL-E (stylized with an interpunct as WALL·E) is a 2008 American computer-animated science fiction film[
        4] produced by Pixar Animation Studios and released by Walt Disney Pictures. It was directed and co-written 
        by Andrew Stanton, produced by Jim Morris, and co-written by Jim Reardon. It stars the voices of Ben Burtt, 
        Elissa Knight, Jeff Garlin, John Ratzenberger, Kathy Najimy, with Sigourney Weaver and Fred Willard. The 
        overall ninth feature film produced by the studio, WALL-E follows a solitary robot on a future, 
        uninhabitable, deserted Earth in 2805, left to clean up garbage. However, he is visited by a probe sent by 
        the starship Axiom, a robot called EVE, with whom he falls in love and pursues across the galaxy. 

        After directing Finding Nemo, Stanton felt Pixar had created believable simulations of underwater physics and 
        was willing to direct a film set largely in space. WALL-E has minimal dialogue in its early sequences; many 
        of the characters do not have voices, but instead communicate with body language and robotic sounds designed 
        by Burtt. The film incorporates various topics including consumerism, corporatocracy, nostalgia, 
        waste management, human environmental impact and concerns, obesity, and global catastrophic risk.[5] It is 
        also Pixar's first animated film with segments featuring live-action characters. Following Pixar tradition, 
        WALL-E was paired with a short film titled Presto for its theatrical release. 

        WALL-E was released in the United States on June 27, 2008. The film received critical acclaim for its 
        animation, story, voice acting, characters, visuals, score, use of minimal dialogue, and scenes of romance.[
        6][7] It was also commercially successful, grossing $521.3 million worldwide over a $180 million budget. It 
        won the 2008 Golden Globe Award for Best Animated Feature Film, the 2009 Hugo Award for Best Long Form 
        Dramatic Presentation,[8] the final Nebula Award for Best Script,[9] the Saturn Award for Best Animated Film 
        and the Academy Award for Best Animated Feature with five nominations. It is considered by many critics as 
        the best film of 2008, [10][11] and to be among the best animated films ever made.[12][13][14] The film 
        topped Time's list of the "Best Movies of the Decade",[15] and in 2016 was voted 29th among 100 films 
        considered the best of the 21st century by 117 film critics from around the world.[16] 

        In 2021, the film was selected for preservation in the United States National Film Registry by the Library of 
        Congress as being "culturally, historically, or aesthetically significant". ''',
        'links': {n + 10, }
    }
]
