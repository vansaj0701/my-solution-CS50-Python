# POETRY EXPLORER
Poetry Explorer is a Python-based interactive application that lets you dive into the world of poetry using the PoetryDB API. Whether you're looking for inspiration or just want to explore random works of literature, this tool provides an easy and fun way to discover poems by random authors, titles, lines, and more.

The app allows you to interact with poetry in a playful way, displaying poems using ASCII art and cowsay animations. It’s perfect for poetry enthusiasts or anyone looking to explore literary gems.


## What is Poetry?
Poetry is a form of literary expression that uses rhythmic, often compact language to convey emotions, ideas, or tell stories. Unlike prose, poetry often employs various devices such as meter, rhyme, metaphor, and symbolism to create a heightened aesthetic experience. It can be written in a structured format with specific rules, like sonnets or haikus, or in free verse with no strict guidelines. Poetry allows writers to express complex feelings and abstract concepts, often evoking a deep emotional response from readers or listeners. Through its unique use of language, poetry captures the beauty, struggle, and intricacies of human experience.


## Table of Contents
+ [Requirements](#requirements)
+ [Menu](#menu)
+ [Random 25 Authors](#random_25_authors)
+ [Random 25 Titles](#random_25_titles)
+ [Random Poem](#random_poem)
+ [Poem by Line](#poem_by_line)
+ [Poem by Line Count](#poem_by_line_count)
+ [Poem by Author](#poem_by_author)
+ [Poem by Title](#poem_by_title)
+ [Installation](#installation)
+ [How to Run](#how_to_run)


## Requirements
Make sure you have the following Python libraries installed:
+ `requests`
+ `cowsay`
+ `art`


## Menu
There are 8 options to choose from
```
------------------------------------------------------------------------------------------------
______  _____  _____  _____ ______ __   __    _____ __   ________  _      _____ ______  _____ ______
| ___ \|  _  ||  ___||_   _|| ___ \\ \ / /   |  ___|\ \ / /| ___ \| |    |  _  || ___ \|  ___|| ___ \
| |_/ /| | | || |__    | |  | |_/ / \ V /    | |__   \ V / | |_/ /| |    | | | || |_/ /| |__  | |_/ /
|  __/ | | | ||  __|   | |  |    /   \ /     |  __|  /   \ |  __/ | |    | | | ||    / |  __| |    /
| |    \ \_/ /| |___   | |  | |\ \   | |     | |___ / /^\ \| |    | |____\ \_/ /| |\ \ | |___ | |\ \
\_|     \___/ \____/   \_/  \_| \_|  \_/     \____/ \/   \/\_|    \_____/ \___/ \_| \_|\____/ \_| \_|



--------------------------------------------- MENU ---------------------------------------------
                1. Random 25 Authors                            5. Poem by Line Count
                2. Random 25 Titles                             6. Poem by Author
                3. Random Poem                                  7. Poem by Title
                4. Poem by Line                                 8. Exit
------------------------------------------------------------------------------------------------
Enter your choice:
```


## Random 25 Authors
Display a list of 25 random authors from the PoetryDB API.

**Sample Output**
```
1 - John Donne
2 - Hugh Henry Brackenridge
3 - John Trumbull
4 - William Browne
5 - Louisa May Alcott
6 - Paul Laurence Dunbar
7 - Arthur Hugh Clough
8 - Robert Louis Stevenson
9 - Jane Austen
10 - Thomas Flatman
11 - Edmund Spenser
12 - Charles Sorley
13 - Ralph Waldo Emerson
14 - Phillis Wheatley
15 - William Vaughn Moody
16 - Amy Levy
17 - Edgar Allan Poe
18 - Henry Vaughan
19 - John Greenleaf Whittier
20 - Walter Savage Landor
21 - Henry David Thoreau
22 - Julia Ward Howe
23 - Anne Bronte
24 - John Milton
25 - William Ernest Henley
```


## Random 25 Titles
Display a list of 25 random poem titles from the PoetryDB API.

**Sample Output**
```
1 - Fragment: Life Rounded With Sleep
2 - The Haunted Palace
3 - If I Were to Own
4 - Lucretius
5 - The Wood-cutter's Night Song
6 - The Butterfly in honored Dust
7 - Spring
8 - A Light Woman
9 - Epistle to Miss Blount, With the Works of Voiture.
10 - You know that Portrait in the Moon --
11 - Sonnet I: Like an Advent'rous Seafarer
12 - Life and Art
13 - London
14 - The Dark Forest
15 - Newstead Abbey
16 - Divine Epigrams: To our Lord, upon the Water Made Wine
17 - In spring and summer winds may blow
18 - Heaven--Haven: A Nun Takes The Veil
19 - Flowers in Winter
20 - An Allegory
21 - Lines to the memory of Richard Boyle, Esq.
22 - Ambition
23 - UPON HIS SISTER-IN-LAW, MISTRESS ELIZABETHHERRICK
24 - Prospice
25 - The Buried Life
```


## Random Poem
Fetch a random poem and display it in an ASCII cow format using cowsay.

**Sample Output**
```
  _____________________________________
 /                                     \
| LIKE the touch of rain she was        |
| On a man's flesh and hair and eyes    |
| When the joy of walking thus          |
| Has taken him by surprise:            |
| With the love of the storm he burns,  |
| He sings, he laughs, well I know how, |
| But forgets when he returns           |
| As I shall not forget her "Go now."   |
| Those two words shut a door           |
| Between me and the blessed rain       |
| That was never shut before            |
| And will not open again.              |
 \                                     /
  =====================================
                                     \
                                      \
                                        ^__^
                                        (oo)\_______
                                        (__)\       )\/\
                                            ||----w |
                                            ||     ||
```


## Poem by Line
Search for a poem by providing a specific line of text.

```
There was an Old Man in a tree
```

**Sample Output**
```
  ________________________________
 /                                \
| There was an Old Man in a tree,  |
| Who was horribly bored by a bee. |
| When they said "Does it buzz?"   |
| He replied "Yes, it does!        |
| It's a regular brute of a bee!"  |
 \                                /
  ================================
                                \
                                 \
                                   ^__^
                                   (oo)\_______
                                   (__)\       )\/\
                                       ||----w |
                                       ||     ||
```


## Poem by Line Count
Retrieve a poem with a specific number of lines.

```
3
```

**Sample Output**
```
 ________________________________
 /                                \
| Of Life to own --                |
| From Life to draw --             |
| But never tough the reservoir -- |
 \                                /
  ================================
                                \
                                 \
                                   ^__^
                                   (oo)\_______
                                   (__)\       )\/\
                                       ||----w |
                                       ||     ||
```


## Poem by Author
Find poems by a particular author.

```
Mary Elizabeth Coleridge
```

**Sample Output**
```
  _______________________________________
 /                                       \
| When wintry winds are no more heard,    |
| And joy's in every bosom,               |
| When summer sings in every bird,        |
| And shines in every blossom,            |
| When happy twilight hours are long,     |
| Come home, my love, and think no wrong! |
| When berries gleam above the stream     |
| And half the fields are yellow,         |
| Come back to me, my joyous dream,       |
| The world hath not thy fellow!          |
| And I will make thee Queen among        |
| The Queens of summer and of song.       |
 \                                       /
  =======================================
                                       \
                                        \
                                          ^__^
                                          (oo)\_______
                                          (__)\       )\/\
                                              ||----w |
                                              ||     ||
```


## Peom by Title
Look up a poem by its title.

```
It Is Not Growing Like A Tree
```

**Sample Output**
```
  ____________________________________________
 /                                            \
| It is not growing like a tree                |
| In bulk doth make Man better be;             |
| Or standing long an oak, three hundred year, |
| To fall a log at last, dry, bald, and sere:  |
| A lily of a day                              |
| Is fairer far in May,                        |
| Although it fall and die that night—         |
| It was the plant and flower of light.        |
| In small proportions we just beauties see;   |
| And in short measures life may perfect be.   |
 \                                            /
  ============================================
                                            \
                                             \
                                               ^__^
                                               (oo)\_______
                                               (__)\       )\/\
                                                   ||----w |
                                                   ||     ||
```


## Installation
1. Install the required dependencies using the following command:
```
pip install requests cowsay art
```
OR
```
pip install -r requirements.txt
```

2. Clone this repository or download the script


## How to Run
1. After downloading/cloning the project, navigate to the directory where the script is located.

2. Run the Python file using:
```
python project.py
```

3. Use the interactive menu to explore various poetry-related options.


## Video Demo: https://youtu.be/s-Q0tJ6UDks
